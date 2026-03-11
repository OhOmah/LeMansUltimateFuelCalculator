"""
Export all tables from a .duckdb file to individual CSV files.
Usage: python export_duckdb_to_csv.py [path/to/file.duckdb] [output_dir]
"""

import sys
import os
import glob
import duckdb


def find_duckdb_file(search_dir="data"):
    """Find a .duckdb file in the given directory."""
    pattern = os.path.join(search_dir, "*.duckdb")
    files = glob.glob(pattern)
    if not files:
        return None
    if len(files) > 1:
        print(f"Multiple .duckdb files found: {files}")
        print(f"Using the first one: {files[0]}")
    return files[0]


def export_tables_to_csv(db_path: str, output_dir: str = None):
    """
    Connect to a DuckDB file, find all tables, and export each to a CSV file.

    Args:
        db_path: Path to the .duckdb file
        output_dir: Directory to write CSV files (defaults to same dir as .duckdb file)
    """
    if not os.path.exists(db_path):
        print(f"Error: File not found: {db_path}")
        sys.exit(1)

    # Default output dir to same folder as the .duckdb file
    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(db_path))

    os.makedirs(output_dir, exist_ok=True)

    print(f"Connecting to: {db_path}")
    con = duckdb.connect(db_path, read_only=True)

    try:
        # Get all table names (excluding views and system tables)
        tables = con.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'main'
              AND table_type = 'BASE TABLE'
            ORDER BY table_name
        """).fetchall()

        if not tables:
            print("No tables found in the database.")
            return

        print(f"Found {len(tables)} table(s): {[t[0] for t in tables]}\n")

        for (table_name,) in tables:
            csv_path = os.path.join(output_dir, f"{table_name}.csv")

            # Use DuckDB's native COPY for fast, reliable CSV export
            con.execute(f"""
                COPY (SELECT * FROM "{table_name}")
                TO '{csv_path}'
                (HEADER, DELIMITER ',')
            """)

            row_count = con.execute(f'SELECT COUNT(*) FROM "{table_name}"').fetchone()[0]
            print(f"  ✓ {table_name} → {csv_path}  ({row_count:,} rows)")

        print(f"\nDone! {len(tables)} CSV file(s) written to: {output_dir}")

    finally:
        con.close()


if __name__ == "__main__":
    # --- Resolve arguments ---
    if len(sys.argv) >= 2:
        db_path = sys.argv[1]
    else:
        # Auto-discover in ./data/
        db_path = find_duckdb_file("data")
        if db_path is None:
            print("Error: No .duckdb file found in the 'data' directory.")
            print("Usage: python export_duckdb_to_csv.py [path/to/file.duckdb] [output_dir]")
            sys.exit(1)
        print(f"Auto-detected database: {db_path}")

    output_dir = sys.argv[2] if len(sys.argv) >= 3 else None

    export_tables_to_csv(db_path, output_dir)

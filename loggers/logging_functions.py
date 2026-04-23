'''
PURPOSE:
Stores all functions in one python file to keep main script easy to read.
'''
import lmu_data
import duckdb

def initDB(db_path:str, schema_name:str, table_name: str):
    con = duckdb.connect(db_path)

    con.exceute(f"CREATE SCHEMA IF NOT EXISTS {schema_name}")

    con.exceute(f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.{table_name} (
            timestamp           DOUBLE      PRIMARY KEY,
            session_start       DOUBLE,
            driver_name         VARCHAR,
            lap_number          INTEGER,
            laps_completed      INTEGER,
            sector              INTEGER,
            lap_dist            DOUBLE,
            last_lap_time       DOUBLE,
            in_pits             BOOLEAN,
            pit_status          INTEGER,
            fuel                DOUBLE,
            fuel_capacity       DOUBLE,
            tire_fl             DOUBLE,
            tire_fr             DOUBLE,
            tire_rl             DOUBLE,
            tire_rr             DOUBLE,
            steering            DOUBLE,
            brake               DOUBLE,
            throttle            DOUBLE,
            accel_x             DOUBLE,
            accel_y             DOUBLE,
            accel_z             DOUBLE,
            vel_x               DOUBLE,
            vel_y               DOUBLE,
            vel_z               DOUBLE
        )
    """)
    
    con.close()

def defineData():
    info = lmu_data.SimInfo()
    tele_data = info.LMUData.telemetry
    scor_data = info.LMUData.scoring

    # Grab data ONLY from the player
    player_index = tele_data.playerVehicleIdx
    player_tele_data = tele_data.telemInfo[player_index]
    player_scor_data = scor_data.vehScoringInfo[player_index]

    return player_scor_data, player_tele_data, tele_data, scor_data

def closeData(player_scor_data, 
            player_tele_data, 
            tele_data, 
            scor_data,):
    '''
    PURPOSE: 
    Closes open data streams
    '''      
    tele_data = None
    scor_data = None
    player_tele_data = None
    player_scor_data = None

    return player_scor_data, player_tele_data, tele_data, scor_data

def pullPlayerName(player_scor_data:str) -> str:
    name = player_scor_data.mDriverName
    return name

def pullLapsCompleted(player_scor_data:int) -> int:
    lapsCompleted = player_scor_data.mTotalLaps
    return lapsCompleted

def pitsIndicator(player_scor_data:bool) -> bool:
    inPits = player_scor_data.mInPits
    return inPits

def pullSector(player_scor_data:int) -> int:
    sector = player_scor_data.mSector
    return sector

def pullStartFinishDist(player_scor_data:float) -> float:
    lapDist = player_scor_data.mLapDist
    return lapDist

def pullLastLapTime(player_scor_data:float) -> float:
    # logs in seconds
    lastLapTime = player_scor_data.mLastLapTime
    return lastLapTime

def pullFuelUsed(player_tele_data:float) -> float:
    fuelUsed = player_tele_data.mFuel
    return fuelUsed

def pullFuelCapacity(player_tele_data:float) -> float:
    fuelCapacity = player_tele_data.mFuelCapacity
    return fuelCapacity

def pullTireWear(player_tele_data:float) -> float:
    # 0=front left, 1=front right, 2=rear left, 3=rear right
    frontLeft = player_tele_data.mWheels[0].mWear
    frontRight = player_tele_data.mWheels[1].mWear
    rearLeft = player_tele_data.mWheels[2].mWear
    rearRight = player_tele_data.mWheels[3].mWear
    return frontLeft, frontRight, rearLeft, rearRight

def pullSteeringAngle(player_tele_data:float) -> float:
    steeringAngle = player_tele_data.mUnfilteredSteering
    return steeringAngle

def pullBrakePosition(player_tele_data:float) -> float:
    brakePosition = player_tele_data.mUnfilteredBrake
    return brakePosition

def pullThrottlePosition(player_tele_data:float) -> float:
    throttlePosition = player_tele_data.mUnfilteredThrottle
    return throttlePosition

def pullAcceleration(player_tele_data:float) -> float:
    accelX = player_tele_data.mLocalAccel.x
    accelY = player_tele_data.mLocalAccel.y
    accelZ = player_tele_data.mLocalAccel.z
    return accelX, accelY, accelZ

def pullVelocity(player_tele_data:float) -> float:
    veloX = player_tele_data.mLocalVel.x
    veloY = player_tele_data.mLocalVel.y 
    veloZ = player_tele_data.mLocalVel.z
    return veloX, veloY, veloZ

def pullPitStatus(player_scor_data:int) -> int:
    # 0=none, 1=request, 2=entering, 3=stopped, 4=exiting, 5=garage
    pitStatus = player_scor_data.mPitState
    return pitStatus

def pullLapNumber(player_tele_data:int) -> int:
    lapNumber = player_tele_data.mLapNumber
    return lapNumber

# TODO: Link to database programaticcly. 

def storeData(data):
    # first note when outlap is happening: 
    print("Out lap in progress, logging will start after out lap is complete")
    player_scor_data, player_tele_data, tele_data, scor_data = defineData()
    out_lap = True
    while out_lap == True:
        
        # take pulled data and save it into a dedicated database
    
        # check if data already exist
        pass



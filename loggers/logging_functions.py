'''
PURPOSE:
Stores all functions in one python file to keep main script easy to read.
'''
import lmu_data

def defineData():
    info = lmu_data.SimInfo()
    tele_data = info.LMUData.telemetry
    scor_data = info.lmuData.scoring

    player_index = tele_data.playerVehicleIdx
    player_tele_data = tele_data.telemInfo[player_index]
    player_scor_data = scor_data.vehScoringInfo[player_index]

    return player_scor_data, player_tele_data, tele_data, scor_data

def closeData(player_scor_data=player_scor_data, 
            player_tele_data=player_tele_data, 
            tele_data=tele_data, 
            scor_data=scor_data,):
    '''
    PURPOSE: 
    Takes data streams and closes 
    '''      
    tele_data = None
    scor_data = None
    player_tele_data = None
    player_scor_data = None

    return None

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
    lapDist = player_sccor_data.mLapDist
    return lapDist

def pullLastLapTime(player_sccor_data:float) -> float:
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


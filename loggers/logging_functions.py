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

def pullPlayerName(player_scor_data = player_scor_data):
    name = player_scor_data.mDriverName
    return name


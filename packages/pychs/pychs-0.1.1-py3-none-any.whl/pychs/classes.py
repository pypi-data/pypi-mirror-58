"""
Python wrapper for Canadian Hydrographic Service (CHS) Water Level Web Services
"""

from zeep import Client
from datetime import datetime, timedelta

OBSERVATIONS_BASE = "https://ws-shc.qc.dfo-mpo.gc.ca/observations"
PREDICTIONS_BASE = "https://ws-shc.qc.dfo-mpo.gc.ca/predictions"

class Observations:
    """

    Attributes
    ----------
    station_id : int
        The Station ID of the Site

    Methods
    -------
    water_level()
        Water level in meters
    water_salinity()
        Water salinity in parts per thousand (0/00)
    water_temperature()
        Water temperature in Celcius degree
    atmospheric_pressure()
        Atmospheric pressure in millibars

    """

    def __init__(self,station_id):
        self.station_id = station_id
        self._station_name = ""
        self.chs_client = Client(OBSERVATIONS_BASE + "?wsdl")
        status = self.chs_client.service.getStatus()
        self.status = status.status
        if (self.status == 'ok'):
            self._name = self.chs_client.service.getName()
            self._info = self.chs_client.service.getInfo()
            self._version = self.chs_client.service.getVersion()

    @property
    def name(self):
        return self._name

    @property
    def info(self):
        return self._info

    @property
    def version(self):
        return self._version

    @property
    def stationName(self):
        return self._station_name

class Predictions:
    """
    
    Attributes
    ----------
    station_id : int
        The Station ID of the Site

    Methods
    -------
    high_low()
        Water levels of high and low tides
    water_level()
        Water Levels each 15 minutes ( :00, :15, :30 and :45 )
    next_high()
        Water levels and time of the next high tide
    next_low()
        Water levels and time of the next low tide

    """

    def __init__(self,station_id):
        self.station_id = station_id
        self._station_name = ""
        self.client = Client(PREDICTIONS_BASE + "?wsdl")
        status = self.client.service.getStatus()
        status = status.status
        if (status == "ok"):
            self._name = self.client.service.getName()
            self._info = self.client.service.getInfo()
            self._version = self.client.service.getVersion()

    @property
    def name(self):
        return self._name

    @property
    def info(self):
        return self._info

    @property
    def version(self):
        return self._version

    @property
    def stationName(self):
        return self._station_name

    def high_low(self):
        # Get the previous and next tides dates, times and heights using UTC
        # Subtract and add 7 hours from the current time to find the search start and end date
        dt_now = datetime.utcnow()
        dt_start = datetime.strftime(dt_now + timedelta(hours=-13),"%Y-%m-%d %H:%M:%S")
        dt_end = datetime.strftime(dt_now + timedelta(hours=13),"%Y-%m-%d %H:%M:%S")

        results = self.client.service.search("hilo",-90,90,-180,180,0.0,0.0,dt_start,dt_end,1,5,True,"station_id="+self.station_id,"asc")
        data = results.data

        # set the station name
        if (self._station_name == ""):
            self._station_name = data[0].metadata[1].value

        output = {}

        for dataElement in data:
            if (datetime.strptime(dataElement.boundaryDate.max,"%Y-%m-%d %H:%M:%S") >= dt_now):
                next_height = dataElement.value
                if (previous_height < next_height):
                    status = "rising"
                    previous_event = "low tide"
                    next_event = "high tide"
                else:
                    status = "falling"
                    previous_event = "high tide"
                    next_event = "low tide"
                output['status'] = status
                output['previous'] = {'event': previous_event, 'height': previous_height, 'date': previous_date}
                output['next'] = {'event': next_event, 'height': next_height, 'date': dataElement.boundaryDate.max}
                break
            else:
                previous_height = dataElement.value
                previous_date = dataElement.boundaryDate.max

        return output

    def water_level(self):
        # Get the water levels for the next hour in 15 minute increments
        dt_now = datetime.utcnow()
        dt_start = datetime.strftime(dt_now,"%Y-%m-%d %H:00:00")
        dt_end = datetime.strftime(dt_now ,"%Y-%m-%d %H:59:59")

        results = self.client.service.search("wl15",-90,90,-180,180,0.0,0.0,dt_start,dt_end,1,4,True,"station_id="+self.station_id,"asc")
        data = results.data

        # set the station name
        if (self._station_name == ''):
            self._station_name = data[0].metadata[1].value

        output = {}
        output['00'] = {'height': data[0].value, 'date': data[0].boundaryDate.max}
        output['15'] = {'height': data[1].value, 'date': data[1].boundaryDate.max}
        output['30'] = {'height': data[2].value, 'date': data[2].boundaryDate.max}
        output['45'] = {'height': data[3].value, 'date': data[3].boundaryDate.max}
        return output

    def next_high(self):
        dt_now = datetime.utcnow()
        dt_start = datetime.strftime(dt_now + timedelta(hours=-13),"%Y-%m-%d %H:%M:%S")
        dt_end = datetime.strftime(dt_now + timedelta(hours=13),"%Y-%m-%d %H:%M:%S")

        results = self.client.service.search("hilo",-90,90,-180,180,0.0,0.0,dt_start,dt_end,1,5,True,"station_id="+self.station_id,"asc")
        data = results.data

        # set the station name
        if (self._station_name == ''):
            self._station_name = data[0].metadata[1].value

        output = {}
        height = 0.0
        for dataElement in data:
            if (datetime.strptime(dataElement.boundaryDate.max,"%Y-%m-%d %H:%M:%S") >= dt_now):
                if (float(dataElement.value) > height):
                    output['next high tide'] = {'height': dataElement.value, 'date': dataElement.boundaryDate.max}
                    break
                else:
                    height = float(dataElement.value)
            else:
                height = float(dataElement.value)
        
        return output
            
    def next_low(self):
        dt_now = datetime.utcnow()
        dt_start = datetime.strftime(dt_now + timedelta(hours=-13),"%Y-%m-%d %H:%M:%S")
        dt_end = datetime.strftime(dt_now + timedelta(hours=13),"%Y-%m-%d %H:%M:%S")

        results = self.client.service.search("hilo",-90,90,-180,180,0.0,0.0,dt_start,dt_end,1,5,True,"station_id="+self.station_id,"asc")
        data = results.data

        # set the station name
        if (self._station_name == ''):
            self._station_name = data[0].metadata[1].value
        
        output = {}
        height = 0.0
        for dataElement in data:
            if (datetime.strptime(dataElement.boundaryDate.max,"%Y-%m-%d %H:%M:%S") >= dt_now):
                if (float(dataElement.value) < height):
                    output['next low tide'] = {'height': dataElement.value, 'date': dataElement.boundaryDate.max}
                    break
                else:
                    height = float(dataElement.value)
            else:
                height = float(dataElement.value)

        return output
'use strict';
/**
 * Makes linter ignore ol variable
 */
if (!window) {
  var ol = '';
}

var earth = new ol.layer.Tile({
  source: new ol.source.OSM()
});



/**
 * Requests the earthquake information for the last seven days from the
 * earthquake USGS database. It returns this as a promise.
 */
function getEarthquakes() {
  var url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson';
  return Promise.resolve($.ajax({
    dataType: 'json',
    url: url,
  }));
}

/**
 * Takes a single earthquake object in as an argument, and returns a simpler
 * earthquake containing only magnitude, age in hours, and an array of XY
 * coordinates.
 */
function formatSingleEarthquake(earthquake) {
  var earthquakeProperies = earthquake.properties;
  var earthquakeGeometry = earthquake.geometry;
  var earthquakeTime = earthquakeProperies.time;
  var earthquakeAgeHours =
    (new Date().getTime() - earthquakeTime) / (1000 * 60 * 60);
  var earthquakeAgeHoursClean = earthquakeAgeHours.toFixed(2);
  var earthquake = {};
  earthquake.magnitude = earthquakeProperies.mag;
  earthquake.ageInHours = earthquakeAgeHoursClean;
  earthquake.XYCoords = earthquakeGeometry.coordinates.slice(0, 2);
  return earthquake;
}

/**
 * Takes in the earthquakes given from the USGS and passes each item into the
 * format single earthquake function (above) as part of a mapping, returning an
 * arry of simple earthquakes.
 */
function formatEarthquakes(earthquakes) {
  var earthquakeFeatures = earthquakes.features;
  var earthquakesAsMagnitutdeAgeCoords = _.map(
    earthquakeFeatures, formatSingleEarthquake
  );
  return earthquakesAsMagnitutdeAgeCoords;
}



/**
 * Creates an array of vector layers to be added to the map variable, by passing
 * in a list of simple earthquakes, and assigning layer values based on the
 * magnitude, age, and location of the earthquake.
 *
 * I have yet to get opacity to work. And messing with new ol.Point
 *
 */
function getDots(earthquakes) {
  var dots = [];
  for (var i = 0; i < earthquakes.length; i += 1) {
    var layer = new ol.layer.Vector({
      source: new ol.source.Vector({
        features: new ol.Feature({
          'geometry': new ol.Point(
            earthquakes[i].XYCoords
          )
        })
      }),
      style: new ol.style.Style({
        image: new ol.style.Circle({
          radius: earthquakes[i].magnitude,
          fill: new ol.style.Fill({color: 'FF5050'})
        })
      })
    });
    dots += layer;
  }
  return dots;
}


/**
 * This function formats the eathquake information into simple earthquakes, then
 * creates a series of vector layers with getDots, and passes them all into a
 * map with an additional earth layer.
 */
function renderEarthquakes(earthquakes) {
  var simpleEarthquakes = formatEarthquakes(earthquakes);
  var dots = getDots(simpleEarthquakes);
  var map = new ol.Map({
    layers: [dots.unshift(earth)],
    target: 'map',
    view: new ol.View({
      center: [0, 0],
      zoom: 2})
  });
}
/**
 * Initiated by the event handler, this function fetches the earthquake data
 * and asynchronistically sends it through the renderEarthquakes function.
 */
function main() {
  getEarthquakes().
  then(renderEarthquakes);
}

$(document).ready(main);

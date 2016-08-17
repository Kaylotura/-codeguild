'use strict';

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
 *
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
 * Initiated by the event handler, this function fetches the earthquake data
 * and asynchronistically manipulates it by extracting information from nested
 * objects & arrays. It then manipulates the date information into an hourly
 * age. It then returns an array of Earthquake Objects, each with a magnitude,
 * location by XY coordinates, and an age.
 */
function formatEarthquakes(earthquakes) {
  var earthquakeFeatures = earthquakes.features;
  var earthquakesAsMagnitutdeAgeCoords = _.map(
    earthquakeFeatures, formatSingleEarthquake
  );
  return earthquakesAsMagnitutdeAgeCoords;
}

/**
 *
 */
function RenderEarthquakes(earthquakes) {
  var simpleEarthquakes = formatEarthquakes(earthquakes);
  var earth = new ol.layer.Tile({
    source: new ol.source.OSM()
  });
  var map = new ol.Map({
    layers: [earth],
    target: 'map',
    view: new ol.View({
      center: [0, 0],
      zoom: 2})
  });

}

function main() {
var earthquakes = getEarthquakes().
then(RenderEarthquakes(earthquakes).

}


  //       layers = []
  //       for (var i = 0; i < x.length; i += 1) {
  //         var layer = new ol.layer.Vector({
  //           source: new ol.source.Vector({
  //             features: new ol.Feature({
  //               'geometry': new ol.Point(
  //                 earthquakesAsMagnitutdeAgeCoords[i].XYCoords
  //               )
  //             })
  //           }),
  //           style: new ol.style.Style({
  //             image: new ol.style.Circle({
  //               radius: earthquakesAsMagnitutdeAgeCoords[i].magnitude,
  //               fill: new ol.style.Fill({color: 'FF5050'})
  //             })
  //           })
  //         })
  //       });
  //     layers += layer



// }

$(document).ready(main);

/**
 * Makes the linter ignore map variable
 */
if (!window) {
  print(map);
}

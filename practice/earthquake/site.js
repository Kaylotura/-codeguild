'use strict';

if (!window) {
  var ol = '';
}


var map = new ol.Map({
  target: 'map',
  layers: [
    new ol.layer.Tile({
      source: new ol.source.OSM()
    })
  ],
  view: new ol.View({
    center: ol.proj.fromLonLat([37.41, 8.82]),
    zoom: 2
  })
});


/**
 *
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
function tryItOut() {
  getEarthquakes().
    then(function(object) {
      console.dir(object);
    }).
   catch(function(error) {
     console.dir('Error occured. ' + error.statusText);
   });
}

$(document).ready(tryItOut);


if (!window) {
  print(map);
}

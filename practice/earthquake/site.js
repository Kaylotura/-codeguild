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
function formatSingleEarthquake(inEarthquake) {
  var effectiveMagnitude = inEarthquake.properties.mag > 0 ?
  inEarthquake.properties.mag : .001;
  return {
    magnitude: effectiveMagnitude,
    ageInHours: (
      (new Date().getTime() - inEarthquake.properties.time) /
       (1000 * 60 * 60)).toFixed(2),
    xyCoords: inEarthquake.geometry.coordinates.slice(0,2)
  };
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
 * This function passes the eathquake information into Format Earthquakes to
 * get simple earthquakes, then creates an array of features for the vectors
 * when rendering the map. Each feature contains the information necisary to
 * render the coordinate of an earthquake, and it's size.
 */
function renderEarthquakes(earthquakes) {
  var simpleEarthquakes = formatEarthquakes(earthquakes);
  $('.map').empty();
  var features = _.map(simpleEarthquakes, function(earthquake) {
    return new ol.Feature({
      'geometry': new ol.geom.Point(
        ol.proj.fromLonLat([earthquake.xyCoords[0],
        earthquake.xyCoords[1]])
      ),
      'size': earthquake.magnitude,
    });
  });

// function renderEarthquakes(earthquakes) {
//   var simpleEarthquakes = formatEarthquakes(earthquakes);
//   $('.map').empty();
//   var count = simpleEarthquakes.length;
//   var features = new Array(count);
//   for (var i = 0; i < count; ++i) {
//     features[i] = new ol.Feature({
//       'geometry': new ol.geom.Point(
//         ol.proj.fromLonLat(
//           [simpleEarthquakes[i].xyCoords[0],
//           simpleEarthquakes[i].xyCoords[1]])
//         ),
//       'size': simpleEarthquakes[i].magnitude,
//     });
//   }


  /**
   *Calculates the style of a rendered vector layer for a given feature. This
   * allows each earthquake to have consistent properties.
   */
  function getStyle(feature) {
    var style = new ol.style.Style({
      image: new ol.style.Circle({
        radius: feature.get('size'),
        fill: new ol.style.Fill({color: '#990000'}),
      })
    });
    return style;
  }

  var vectorSource = new ol.source.Vector({
    features: features,
  });

  var vector = new ol.layer.Vector({
    source: vectorSource,
    style: function(feature) {
      return getStyle(feature);
    }
  });

  var map = new ol.Map({
    layers: [earth, vector],
    target: document.getElementById('map'),
    view: new ol.View({
      center: [0, 0],
      zoom: 2
    })
  });
  // });
}

/**
 * Initiated by the event handler, this function fetches the earthquake data
 * and asynchronistically sends it through the renderEarthquakes function.
 */
function mapEarthquakes() {
  getEarthquakes().
  then(renderEarthquakes);
}

$(document).ready(mapEarthquakes);

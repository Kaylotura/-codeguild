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
 * Earth renders fine, but dots don't show up at all... I'm kind of at a loss on
 * what's going wrong.
 *
 */
function getDots(earthquakes) {
  var dots = [earth];
  for (var i = 0; i < earthquakes.length; i += 1) {
    var layer = new ol.layer.Vector({
      source: new ol.source.Vector({
        features: new ol.Feature({
          'geometry': new ol.geom.Point(
            earthquakes[i].XYCoords
          )
        })
      }),
      style: new ol.style.Style({
        image: new ol.style.Circle({
          radius: 2 + earthquakes[i].magnitude,
          fill: new ol.style.Fill({color: 'FF5050'}),
          stroke: new ol.style.Stroke({color: '#FFFFFF', width: 1}),
          opacity: 1 - (earthquakes[i].age / 168)
        })
      })
    });
    dots.push(layer);
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
  console.dir(dots);
  $('.map').empty();
  // var map = new ol.Map({
  //   layers: dots,
  //   target: 'map',
  //   view: new ol.View({
  //     center: [0, 0],
  //     zoom: 2})
  var count = simpleEarthquakes.length;
  var features = new Array(count);
  for (var i = 0; i < count; ++i) {
    features[i] = new ol.Feature({
      'geometry': new ol.geom.Point(
          [simpleEarthquakes[i].XYCoords[0] * 110000, simpleEarthquakes[i].XYCoords[1] * 110000]),
    });
  }

  var style = new ol.style.Style({
    image: new ol.style.Circle({
      radius: 10,
      fill: new ol.style.Fill({color: '#FF0606'}),
    })
  });

  var vectorSource = new ol.source.Vector({
    features: features,
  });
  var vector = new ol.layer.Vector({
    source: vectorSource,
    style: style
  });

  var map = new ol.Map({
    layers: [earth, vector],
    target: document.getElementById('map'),
    view: new ol.View({
      center: [0, 0],
      zoom: 2
    })
  });

  var style = new ol.style.Style({
    image: new ol.style.Circle({
      radius: 10,
    })
  });





  // });
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

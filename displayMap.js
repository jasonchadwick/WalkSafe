"use strict";
function createPath()
{
let locs = [];

fetch("./locations.json")
    .then(function(resp) {
      return resp.json();
    })
    .then(function(data) {
        locs = data.locations;
    });
// above: load from json file using fetch - needs to be fetched from server

L.mapquest.key = 'KEY';
var map = L.mapquest.map('map', {
  center: [40.7,-73.9],
  layers: L.mapquest.tileLayer('dark'),
  zoom: 12
});

var directions = L.mapquest.directions();
directions.setLayerOptions({
  startMarker: {
    icon: 'circle',
    iconOptions: {
      size: 'sm',
      primaryColor: '#1fc715',
      secondaryColor: '#1fc715',
      symbol: 'A'
    }
  },
  endMarker: {
    icon: 'circle',
    iconOptions: {
      size: 'sm',
      primaryColor: '#e9304f',
      secondaryColor: '#e9304f',
      symbol: 'B'
    }
  },
  routeRibbon: {
    color: "#2aa6ce",
    opacity: 1.0,
    showTraffic: false
  },
  alternateRouteRibbon: {
    opacity: 1.0
  },
});

directions.route({
  locations: locs
});
}
// Initialize and add the map
function initMap() {
  // The location of Uluru
  const uluru = { lat: 39.728958, lng: -121.838783 };
  // The map, centered at Uluru
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 8,
    center: uluru,
  });
}
window.initMap = initMap;
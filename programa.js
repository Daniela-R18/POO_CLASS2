var map = L.map('map').setView([4.60971, -74.08175], 13); // Bogotá

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

// Marker con popup cute
L.marker([4.60971, -74.08175]).addTo(map)
  .bindPopup('<b>¡Aquí estoy!</b><br>Mi ciudad 💜')
  .openPopup();
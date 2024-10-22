
document.addEventListener('DOMContentLoaded', function load_Map(){
    
    var map = L.map('main-map').setView([17.6868, 83.2185], 12);

    
    var openStreetMap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    });

    var openSeaMap = L.tileLayer('https://tiles.openseamap.org/seamark/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://www.openseamap.org">OpenSeaMap</a> contributors'
    });

    openStreetMap.addTo(map);
    openSeaMap.addTo(map);

});
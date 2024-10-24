
class Contact{
    constructor(id, type, designator, current_loc, heading, last_report_time, speed, history, meta, status){
        this.id = id;
        this.type = type;
        this.designator = designator;
        this.current_loc = current_loc;
        this.heading = heading;
        this.last_report_time = last_report_time;
        this.speed = speed;
        this.history = history;
        this.meta = meta;
        this.status = status;
    }
}

var current_Contacts = new Map();
var markers_ = new Map();
var map = null;

document.addEventListener('DOMContentLoaded', async function load_Map(){
    
    status_('[+] Loading Map...');

    map = L.map('main-map', {
        fullscreenControl: {
            pseudoFullscreen: true // if true, fullscreen to page width and height
        },
    }).setView([17.6868, 83.2185], 12);

    
    var openStreetMap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    });

    var openSeaMap = L.tileLayer('https://tiles.openseamap.org/seamark/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://www.openseamap.org">OpenSeaMap</a> contributors'
    });

    var darkTileLayer = L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        maxZoom: 19,
        subdomains: 'abcd'
    });


    openStreetMap.addTo(map);
    openSeaMap.addTo(map);
    darkTileLayer.addTo(map);

    // var graticule = L.graticule({
    //     interval: 0.2, // Set the interval for grid lines
    //     style: {
    //         color: 'white', // Color of the grid lines
    //         weight: 100
    //     }
    // }).addTo(map);

    // map.addControl(new L.Control.Fullscreen());

        // Detect when fullscreen is entered or exited
    map.on('enterFullscreen', function() {
        console.log('Entered fullscreen mode');
    });

    map.on('exitFullscreen', function() {
        console.log('Exited fullscreen mode');
    });

    status_('[.] Map Loaded.');

    status_('[+] Loading contacts...');

    var contacts = await eel.fetch_all()();

    status_('Fetched contacts. Plotting...')

    plot_contacts_fresh(contacts);

    // statusdiv.textContent = contacts[0][2];

});


function status_(sts_txt=""){
    var statusdiv = document.getElementById('statusdiv');
    statusdiv.textContent = sts_txt;
}

function plot_contacts_fresh(contacts=null){
    // console.log(contacts);
    if (contacts != null){
        current_Contacts = new Map();
        markers_ = new Map();
        contacts.forEach(contact => {
            var id = contact[0];
            var type = contact[1];
            var desig = contact[2];
            var loc = null;
            if (contact[3] != null){
                loc = [Number(contact[3].split(",")[0]), 
                Number(contact[3].split(", ")[1])]
            }
            var heading = contact[4];
            var lastreport = contact[5];
            var speed = contact[6];
            var history = contact[7];
            var meta = contact[8];
            var status = contact[9];
            var thisContact = new Contact(
                id, type, desig, loc, heading, lastreport, speed, history, meta, status
            );
            current_Contacts.set(thisContact.id, thisContact);
            for(const [key, contact] of current_Contacts){
                plot_this_contact(contact);
            }
            // console.log(thisContact);
        });    
    } else{
        // current_Contacts.set(thisContact.id, thisContact);
        removeAllMarkers();
        for(const [key, contact] of current_Contacts){
            plot_this_contact(contact, new_marker_=false);
        }
    }
    console.log(markers_);
    
}

function add_contact(contact){
    var id = contact[0];
    var type = contact[1];
    var desig = contact[2];
    var loc = null;
    if (contact[3] != null){
        loc = [Number(contact[3].split(",")[0]), 
        Number(contact[3].split(", ")[1])]
    }
    var heading = contact[4];
    var lastreport = contact[5];
    var speed = contact[6];
    var history = contact[7];
    var meta = contact[8];
    var status = contact[9];
    var thisContact = new Contact(
        id, type, desig, loc, heading, lastreport, speed, history, meta, status
    );
    current_Contacts.set(thisContact.id, thisContact);
    plot_this_contact(thisContact);
    // console.log(thisContact);
}

function getAllMarkers() {

    var allMarkersObjArray = []; // for marker objects
    var allMarkersGeoJsonArray = []; // for readable geoJson markers

    map.eachLayer(function (layer) {
        if (layer instanceof L.Marker) { // Check if the layer is a marker
            allMarkersObjArray.push(layer); // Add marker object to array
            allMarkersGeoJsonArray.push(JSON.stringify(layer.toGeoJSON())); // Convert marker to GeoJSON and add to array
        }
    });

    return allMarkersObjArray;
}

function remove_marker(contactid){
    
    console.log("Remove marker called: ", markers_.get(contactid + "_marker_id_"));
    var allmarkers = getAllMarkers();

    allmarkers.forEach(marker => {
        console.log(marker.markerId);
        if (marker.markerId == contactid + "_marker_id_"){
            marker.remove();
        }
    });
}

function plot_this_contact(contact, new_marker_=true){
    if(contact.current_loc != null){
        if (new_marker_){
            var status_icon_colormap = new Map([
                ['routine','blue'],
                ['confidential', 'purple'],
                ['urgent', 'orange'],
                ['immediate', 'red'],
                ['secret', 'darkpurple'],
                ['unknown', 'green']
            ]);
    
            if (contact.status != null){
                var markerIcon_ship = L.AwesomeMarkers.icon({
                    icon:'ship', // ship, rocket, plane, motocycle, fighter-jet, car, bus, bicycle, automobile
                    markerColor:status_icon_colormap.get(contact.status), // red, darkred, orange, green, darkgreen, blue, purple, darkpurple, cadetblue
                    prefix: 'fa',
                });
            } else{
                var markerIcon_ship = L.AwesomeMarkers.icon({
                    icon:'ship', // ship, rocket, plane, motocycle, fighter-jet, car, bus, bicycle, automobile
                    markerColor:status_icon_colormap.get('unknown'), // red, darkred, orange, green, darkgreen, blue, purple, darkpurple, cadetblue
                    prefix: 'fa',
                });
            }
    
            var marker_this_contact_ = L.marker([contact.current_loc[0], contact.current_loc[1]], {icon : markerIcon_ship});

            marker_this_contact_.addTo(map);

            var this_contact_marker_popup_ = document.createElement('div');
            this_contact_marker_popup_.style.backgroundColor = 'rgb(46, 46, 46)';
            this_contact_marker_popup_.style.color = "antiquewhite";
            this_contact_marker_popup_.style.fontFamily = "Arial, Helvetica, sans-serif";
            this_contact_marker_popup_.style.fontSize = "small";
            this_contact_marker_popup_.style.padding = "5px 5px";
            this_contact_marker_popup_.style.borderRadius = "5px";
            this_contact_marker_popup_.style.border = "1px solid antiquewhite";
            this_contact_marker_popup_.style.width = "100%";
            this_contact_marker_popup_.textContent = contact.designator;
    
            marker_this_contact_.markerId = contact.id+"_marker_id_";

            marker_this_contact_.bindPopup(this_contact_marker_popup_, {
                autoClose: false,
            });
            marker_this_contact_.openPopup();
            
            // const markerpopup = L.popup({
            //     autoClose: true,
            //     closeOnClick: false
            // })
            // .setLatLng(contact.current_loc)
            // .setContent(this_contact_marker_popup_)
            // .addTo(map);
    
            // // Open popup automatically
            // marker_this_contact_.bindPopup(markerpopup).openPopup();
    
            marker_this_contact_.on('mouseover', function(){
                marker_this_contact_.openPopup();
                show_dets_marker(contact);
    
            });
    
            marker_this_contact_.on('click', function(){
                // show_dets_marker(contact);
                alert("removing contact: " + String(contact.designator));
                remove_marker(contact.id);
                // map.removeLayer(marker_this_contact_);
            });
    
            markers_.set(contact.id+"_marker_id_",  marker_this_contact_);

            if (contact.heading != null){
                addHeadingAndCompass(
                    markers_.get(contact.id+"_marker_id_"), 
                    String(contact.heading), 
                    String(contact.speed),
                    status_icon_colormap.get(contact.status)
                );
            }
            
        } else{
            markers_.get(contact.id + "_marker_id_").addTo(map);
        }
        
    } else{
        return "null location";
    }
}

function addHeadingAndCompass(marker, heading_param, linecolor) {
    const heading = parseFloat(heading_param.replace('°', ''));; // Example heading, you can set this dynamically
    const radius = 15; // Radius for the compass ring

    // Create the compass ring (div)
    const compassRing = L.divIcon({
        className: 'compass-ring',
        iconSize: [radius * 2, radius * 2],
        iconAnchor: [radius, radius],
        html: "<div style='color:antiquewhite; font-size:medium; font-weight:bold;'>" + heading_param + "</div>"
    });

    // Add the compass ring to the map
    const compassMarker = L.marker(marker.getLatLng(), { icon: compassRing });
    marker.compassMarker = compassMarker;
    compassMarker.addTo(map);

    // Calculate the end point of the heading line
    const headingRad = (heading - 90) * (Math.PI / 180); // Convert to radians
    const lineEndLat = marker.getLatLng().lat + Math.sin(headingRad) * 0.05; // 0.1 is the distance in degrees
    const lineEndLng = marker.getLatLng().lng + Math.cos(headingRad) * 0.05;

    // Draw the heading line
    const headingline = L.polyline([marker.getLatLng(), [lineEndLat, lineEndLng]], { color: "red", weight: 3 });
    marker.headingline = headingline;
    headingline.addTo(map);

    marker.on('remove', function (){
        map.removeLayer(headingline);
        map.removeLayer(compassMarker);
    });
}

function capitalize(str) {
    if (!str) return str; // Check for empty string
    return str.toUpperCase().replace(/^(.)(.*)$/, (match, p1, p2) => p1.toUpperCase() + p2.toLowerCase());
}

function show_dets_marker(contact){
    // show basic properties of contact
    var this_marker_report_element_ = document.getElementById("report_box");
    var this_marker_properties_element_ = document.getElementById('stat_box');
    var showtext = "";
    showtext += "<p style='font-size:25px'; font-weight:bold;>" + contact.designator + "<br></p>";
    showtext += "<div style='width:98%'; height:100%; overflow:auto;>";
    var status_icon_colormap = new Map([
        ['routine','blue'],
        ['confidential', 'purple'],
        ['urgent', 'orange'],
        ['immediate', 'red'],
        ['secret', 'darkpurple'],
        ['unknown', 'green']
    ]);
    if (contact.status != null){
        showtext += "<div style='background-color:" + status_icon_colormap.get(contact.status) + "; font-size:25px'; font-weight:bold;'>" + capitalize(String(contact.status)) + " </div> <br>";
    }
    if (contact.current_loc != null){
        showtext += "LAT: " + String(contact.current_loc[0]) + " LON: " + String(contact.current_loc[1]) + "<br><br>";
    }
    if (contact.heading != null){
        showtext += "HEADING: " + contact.heading + "<br><br>";
    }
    if (contact.last_report_time != null){
        showtext += "LAST REPORTED: " + String(contact.last_report_time) + "<br><br>"
    }
    if (contact.speed != null){
        showtext += "SPEED: " + String(contact.speed) + "<br><br>";
    }
    showtext += "</div>"
    var report_text = "";
    if (contact.meta != null){
        report_text += String(contact.meta) + "<br><br>";
    }
    this_marker_report_element_.innerHTML = report_text;
    this_marker_properties_element_.innerHTML = "";
    this_marker_properties_element_.innerHTML = showtext;
}


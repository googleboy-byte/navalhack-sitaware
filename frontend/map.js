
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

document.addEventListener('DOMContentLoaded', async function load_Map(){
    
    status_('[+] Loading Map...');

    var map = L.map('main-map').setView([17.6868, 83.2185], 12);

    
    var openStreetMap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    });

    var openSeaMap = L.tileLayer('https://tiles.openseamap.org/seamark/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://www.openseamap.org">OpenSeaMap</a> contributors'
    });

    openStreetMap.addTo(map);
    openSeaMap.addTo(map);

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

function plot_contacts_fresh(contacts){
    // console.log(contacts);
    current_Contacts = new Map();
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
        console.log(thisContact);
    });
}

function plot_this_contact(contact){

}


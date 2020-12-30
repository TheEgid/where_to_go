const map = L.map('map');
map.setView([55.753989, 37.623191], 11);

L.tileLayer.provider('OpenStreetMap.Mapnik').addTo(map);

const sidebar = L.control.sidebar('sidebar', {
    closeButton: true,
    position: 'right'
});
map.addControl(sidebar);

// FIXME should be hidden in production mode
L.control.custom({
    position: 'bottomleft',
    content: `
        <label>
            <input name="debug" type="checkbox" ${log.getLevel()<=1 && 'checked'}/>
            Отладка
        </label>`,
    style: {
        padding: '10px',
        background: 'rgba(255, 255, 255, 0.7)',
    },
    events: {
        click: event => {
            if (event.target.name == 'debug'){
                let level = event.target.checked && 'debug' || 'warn';
                log.setLevel(level);
                console.log(`Set log level: ${level}`)
            }
        },
    }
}).addTo(map);

function loadJSON(elementId){
    let element = document.getElementById(elementId);

    if (!element){
        log.error(`Not found element with id '${elementId}'.`)
        return null;
    }

    return JSON.parse(element.textContent);
}

let places = loadJSON('places-geojson');
log.debug('Load GeoJSON for places', places);


L.geoJSON(places, {
    pointToLayer: function(geoJsonPoint, latlng) {
        if (geoJsonPoint.geometry.type != "Point"){
            return
        }

        let color = geoJsonPoint.properties.color || 'red';

        var pulsingIcon = L.icon.pulse({
            iconSize: [12, 12],
            color: color,
            fillColor: color,
            heartbeat: 2.5,
        });

        let marker = L.marker(latlng, {
            icon: pulsingIcon,
            riseOnHover: true,
        });

        marker.bindTooltip(geoJsonPoint.properties.title);
        marker.bindPopup(function (layer) {
            return geoJsonPoint.properties.title;
        })

        marker.on('click', function(event){
            log.debug('Feature selected', geoJsonPoint);
            sidebar.show();
            loadPlaceInfo(geoJsonPoint.properties.placeId, geoJsonPoint.properties.detailsUrl);
        });
        return marker;
    }
}).addTo(map);

const sidebarApp = new Vue({
    el: '#sidebar-app',
    template: document.getElementById('app-template').innerHTML,
    data: {
        loadingPlaceId: null,
        selectedPlace: null,  // object with attributes specified below
        // title
        // placeId
        // imgs
        // short_description
        // long_description
    },
    computed: {
        promptVisible: function () {
            return !this.loading && !this.selectedPlace;
        },
        loading: function () {
            return this.loadingPlaceId !== null;
        },
        mainPhotoSrc: function () {
            if (!this.selectedPlace || !this.selectedPlace.imgs.length) {
                return null;
            }
            return this.selectedPlace.imgs[0];
        },
        carouselImgs: function () {
            if (!this.selectedPlace || !this.selectedPlace.imgs.length) {
                return [];
            }
            return this.selectedPlace.imgs.slice(1);
        },
    },
    updated: function () {
        this.$nextTick(function () {
            // Код, будет запущен только после обновления всех представлений
            $('#place-photos').carousel();
        })
    },
    methods: {
        handlePhotosClick: function (slideId = 'next') {
            // default event handlers of Bootstrap Carousel conflict with Leaflet
            // so custom handler will mimic expected carousel behaviour
            $('#place-photos').carousel(slideId);
        }
    },
});

map.on('click', function () {
    sidebarApp.selectedPlace = null;
    sidebarApp.loadingPlaceId = null;
})

async function loadPlaceInfo(placeId, detailsUrl){
    sidebarApp.selectedPlace = null;
    sidebarApp.loadingPlaceId = placeId;

    try {
        let response = await fetch(detailsUrl);

        if (!response.ok){
            return;
        }

        let data = await response.json();

        if (sidebarApp.loadingPlaceId != placeId){
            // Place loading was cancelled by user
            return
        }

        sidebarApp.selectedPlace = {
            title: data.title,
            placeId: placeId,
            imgs: data.imgs || [],
            short_description: data.description_short,
            long_description: data.description_long,
        };
    } finally {
        if (sidebarApp.loadingPlaceId == placeId){
            sidebarApp.loadingPlaceId = null;
        }
    }
}
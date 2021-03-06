let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: new google.maps.LatLng(-33.91722, 151.23064),
    zoom: 16,
  });

  const iconBase =
    "https://developers.google.com/maps/documentation/javascript/examples/full/images/";
  const icons = {
    parking: {
      icon: iconBase + "parking_lot_maps.png",
      type:"Parking"
    },
    library: {
      icon: iconBase + "library_maps.png",
    },
    info: {
      icon: iconBase + "info-i_maps.png",
    },
  };
  const features = [
    {
        placeName:"<div><h3>A1 Location</h3></div><a href=http://111.92.33.219:60001/cgi-bin/snapshot.cgi?chn=0&u=admin&p=&q=0&1642531519>camera link</a>",
      position: new google.maps.LatLng(-33.91721, 151.2263),
      type: "info",
    },
    {
        placeName:"test",
      position: new google.maps.LatLng(-33.91539, 151.2282),
      type: "info",
    },
    {
        placeName:"test",
      position: new google.maps.LatLng(-33.91747, 151.22912),
      type: "info",
    },
    {
        placeName:"test",
      position: new google.maps.LatLng(-33.9191, 151.22907),
      type: "info",
    },
    {
        placeName:"test",
      position: new google.maps.LatLng(-33.91725, 151.23011),
      type: "info",
    },
    {
        placeName:"test",
      position: new google.maps.LatLng(-33.91872, 151.23089),
      type: "info",
    },
    {
        placeName:"test",
      position: new google.maps.LatLng(-33.91784, 151.23094),
      type: "info",
    },
    {
        placeName:"test",
      position: new google.maps.LatLng(-33.91682, 151.23149),
      type: "info",
    },
    {
        placeName:"test",
      position: new google.maps.LatLng(-33.9179, 151.23463),
      type: "info",
    },
    {
        placeName:"test",
      position: new google.maps.LatLng(-33.91666, 151.23468),
      type: "info",
    },
    {
        placeName:"test",
      position: new google.maps.LatLng(-33.916988, 151.23364),
      type: "info",
    },
    {
        placeName:"test",
      position: new google.maps.LatLng(-33.91662347903106, 151.22879464019775),
      type: "parking",
    },
    {
        placeName:"test",
      position: new google.maps.LatLng(-33.916365282092855, 151.22937399734496),
      type: "parking",
    },
    {
        placeName:"test",
      position: new google.maps.LatLng(-33.91665018901448, 151.2282474695587),
      type: "parking",
    },
    {
        placeName:"test",
      position: new google.maps.LatLng(-33.919543720969806, 151.23112279762267),
      type: "parking",
    },
    
  ];

  // Create markers.
  for (let i = 0; i < features.length; i++) {
      var contentString ='<h3>'+features[i].placeName+'</h3>'
    const marker = new google.maps.Marker({
      position: features[i].position,
      icon: icons[features[i].type].icon,
      map: map,
    });

    const infowindow = new google.maps.InfoWindow({
    content: contentString,
  });
  marker.addListener("click", () => {
    infowindow.open({
      anchor: marker,
      map,
      shouldFocus: false,
    });
  });
  }
}
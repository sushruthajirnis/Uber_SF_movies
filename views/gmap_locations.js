
var BASE_URL = "http://localhost:5000/sfinmovies/api/";
var map;	
function initialize(){
	map=initializeMap();
	add_markers();
      }
google.maps.event.addDomListener(window, 'load', initialize);	
function initializeMap() {
	 var mapOptions = {
              zoom: 8,
                  center: new google.maps.LatLng(-34.397, 150.644)
                    };
                      return new google.maps.Map(document.getElementById('map-canvas'),
                            mapOptions);

	
}





function add_markers(){
query_string = "v1/search?title=Flower Drum Song";
     $.getJSON(BASE_URL + query_string, function(data) {
	var movies = data.movies;
	
        for (var i = 0; i < movies.length; i++) {

            var movie = movies[i];
	
            
            // Create marker
            var marker = new google.maps.Marker({
                position : new google.maps.LatLng(movie.latitude,
                                                  movie.longitude),
                map : map
               
 	         	  });

		}
	
	});
}



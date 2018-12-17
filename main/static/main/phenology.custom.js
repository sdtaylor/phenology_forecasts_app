
//leaflet map stuff
//var map;
//var map_image_layer;
//var map_image_bounds = [[24.0625,-125.0208],[49.9375,-66.479]];
var debug=false;

var current_species = "acer_rubrum";
var current_phenophase = 371;
var current_issue_date = "2018-12-14";



function update_current_info(selected_data){
    if("phenophase" in select_data){
       current_phenophase = select_data["phenophase"];
    }
    if("issue_date" in select_data){
       current_issue_date = select_data["issue_date"];
    }
    if("phenophase" in select_data){
       current_species = select_data["species"];
    }
    
    draw_map()
}

          
function init_page() {
    log_text("initializing")
    draw_map();

    console.log(window.location.href)


}

// get current status of a specified dropdown
function get_selection(select_id) {
    var s = document.getElementById(select_id);
    return s.options[s.selectedIndex].value;
}


function log_text(message) {
    if (debug){
        document.getElementById("log_output").innerHTML += '<br>' + message;
    }
}

//This updates the text info below all the menus
function update_forecast_info(message) {
    document.getElementById("forecast_info").innerHTML = '<h4><b>' + message + '</b></h4>';
}

//This updates the text info below all the menus
function update_forecast_permalinks(clear=false, issue_date, species, phenophase) {
 //   first_line = '<a href="/2018-12-03/acer_rubrum/371">Link to this forecast</a>'
 //   second_line = '<a href="/latest/acer_rubrum/371">Latest forecast for this species</a>'
    if (clear) {
        document.getElementById("forecast_permalinks").innerHTML = '';
    } else {
        first_line = '<a href="/'+issue_date+'/'+species+'/'+phenophase+'">Direct link to this forecast</a>';
        second_line = '<a href="/latest/'+species+'/'+phenophase+'">Latest forecast for this species</a>';
        document.getElementById("forecast_permalinks").innerHTML = '<br>' + first_line + '<br>' + second_line;
    }
}


function draw_map() {
    //get info to display
    log_text("drawing map")
    var map_type = get_selection("map_type_select");
    var issue_date = get_selection("issue_date_select");
    var species = get_selection("species_select");
    var phenophase = get_selection("phenophase_select");
    
    log_text("#######################")
    log_text("selected map_type: "+map_type);
    log_text("selected issue_date: "+issue_date);
    log_text("selected species: "+species);
    log_text("selected phenophase: "+phenophase);


    //var current_type = current_map_type()
    if (current_map_type() == map_type) {
        log_text("map types equal");
    } else {
        log_text("map types dont equal");
        toggle_maps();
    }
    var prior_image_layer;
    var current_image_layer;
    if (map_type=='interactive') {
        clear_map();
        var image_filename = species+'_'+phenophase+'_'+issue_date+'_map.png';
        var image_url = 'images/'+issue_date+'/'+image_filename;
        
        if (image_metadata.available_images.indexOf(image_filename) == -1){
            update_forecast_info("Forecast not available");
            log_text("map not available: "+image_filename);
        } else {
            update_forecast_info("");
            log_text('setting image: ' + image_filename);
        }
        
        map_image_layer = L.imageOverlay(image_url, map_image_bounds, {opacity: 0.7});
        map_image_layer.addTo(map);
    } else {
        //construct image url
        var forecast_availability;
        
        var image_filename_prediction = species+'_'+phenophase+'_'+issue_date+'_prediction.png';
        var image_url_prediction = '/static/main/images/'+issue_date+'/'+image_filename_prediction;
        
        var image_filename_uncertainty = species+'_'+phenophase+'_'+issue_date+'_uncertainty.png';
        var image_url_uncertainty = '/static/main/images/'+issue_date+'/'+image_filename_uncertainty;
        
        var image_filename_anomaly = species+'_'+phenophase+'_'+issue_date+'_anomaly.png';
        var image_url_anomaly = '/static/main/images/'+issue_date+'/'+image_filename_anomaly;
        
        //check availability using primary image name as a lookup. image names are unique to all forecats. 
        $.getJSON('/api/forecasts/detail/' + image_filename_prediction, 
        function(json) {
            update_forecast_info("");
            update_forecast_permalinks(clear=false, issue_date, species, phenophase);
            log_text('setting image: ' + image_url);
        }).fail(function(failure) {
            update_forecast_info("Forecast not available");
            update_forecast_permalinks(clear=true);
            log_text("image not available: "+image_filename);
        })
        
        //set image
        $('#static_map_prediction').attr('src',image_url_prediction);
        $('#static_map_anomaly').attr('src',image_url_anomaly);
        $('#static_map_uncertainty').attr('src',image_url_uncertainty);
    }
}

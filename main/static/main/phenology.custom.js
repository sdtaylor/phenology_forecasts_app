var debug=false;
var current_phenophase;

function update_phenophase(p){
    current_phenophase=p;
    init_page(phenophase_update_only=true);
}

function update_phenophase_buttons(available_phenophases){
        if(available_phenophases.includes(371)){
            $('button#leaf-button').prop('disabled', false);
        } else {
            $('button#leaf-button').prop('disabled', true);
        }
        if(available_phenophases.includes(501)){
            $('button#flower-button').prop('disabled', false);
        } else {
            $('button#flower-button').prop('disabled', true);
        }
        if(available_phenophases.includes(498)){
            $('button#fall-button').prop('disabled', false);
        } else {
            $('button#fall-button').prop('disabled', true);
        }
        if(available_phenophases.includes(390)){
            $('button#fruit-button').prop('disabled', false);
        } else {
            $('button#fruit-button').prop('disabled', true);
        }
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
function update_forecast_permalinks(clear=false, issue_date, species) {
 //   first_line = '<a href="/2018-12-03/acer_rubrum/371">Link to this forecast</a>'
 //   second_line = '<a href="/latest/acer_rubrum/371">Latest forecast for this species</a>'
    if (clear) {
        document.getElementById("forecast_permalinks").innerHTML = '';
    } else {
        first_line = '<a href="/'+issue_date+'/'+species+'/'+'">Direct link to this forecast</a>';
        second_line = '<a href="/latest/'+species+'/'+'">Latest forecast for this species</a>';
        document.getElementById("forecast_permalinks").innerHTML = '<br>' + first_line + '<br>' + second_line;
    }
}

function set_images(issue_date, species, phenophase){
    log_text("#######################")
    log_text("selected issue_date: "+issue_date);
    log_text("selected species: "+species);
    log_text("selected phenophase: "+phenophase);

    update_forecast_permalinks(clear=false, issue_date=issue_date, species=species);
    
    //construct image urls
    var image_filename_prediction = species+'_'+phenophase+'_'+issue_date+'_prediction.png';
    var image_url_prediction = '/static/main/images/'+issue_date+'/'+image_filename_prediction;
    
    var image_filename_uncertainty = species+'_'+phenophase+'_'+issue_date+'_uncertainty.png';
    var image_url_uncertainty = '/static/main/images/'+issue_date+'/'+image_filename_uncertainty;
    
    var image_filename_anomaly = species+'_'+phenophase+'_'+issue_date+'_anomaly.png';
    var image_url_anomaly = '/static/main/images/'+issue_date+'/'+image_filename_anomaly;
    
    //set images
    $('#static_map_prediction').attr('src',image_url_prediction);
    $('#static_map_anomaly').attr('src',image_url_anomaly);
    $('#static_map_uncertainty').attr('src',image_url_uncertainty);
    
    
    
}

function init_page(phenophase_update_only=false) {
    //get info to display
    log_text("drawing map")
    var issue_date = get_selection("issue_date_select");
    var species = get_selection("species_select");
    
    if(phenophase_update_only){
        set_images(issue_date, species, current_phenophase);
    } else {
    //Get the available phenophases for this issue_date,species
    query_str = '/api/forecasts/detail/?issue_date='+issue_date+'&species='+species;
    $.getJSON(query_str, 
        function(json){
            var available_phenophases=[];
            for(var i=0; i<json.length;i++){
                available_phenophases.push(json[i]['phenophase']);
            }
            update_phenophase_buttons(available_phenophases);
            current_phenophase=available_phenophases[0];
            
            set_images(issue_date, species, current_phenophase);
        }
      )
    }
}

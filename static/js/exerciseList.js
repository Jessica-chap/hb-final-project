"use strict";

  const addItemToTable = (exercise, sets, reps, 
                          repunit, info, weight,
                          weightunit, equipment) => {
    $('#user-exercise-selections').append("<tr>" +
            "<td>" + exercise + "</td>" +
            "<td>" + sets + "</td>" +
            "<td>" + reps + "</td>" +
            "<td>" + repunit + "</td>" +
            "<td>" + info + "</td>" +
            "<td>" + weight + "</td>" +
            "<td>" + weightunit + "</td>" +
            "<td>" + equipment + "</td>" +
            "</tr>");
  };


  $('#exercise-form').on('submit', (evt) => {
    evt.preventDefault();
    console.log(evt);
    const formInputs = {
      //'server .get requests : assign from HTML
        'api_exercise_selection': $("#api_exercise_selection").val(),
        'exercise_sets': $("#exercise_sets").val(),
        'exercise_reps': $("#exercise_reps").val(),
        'exercise_repunit': $("#exercise_repunit").val(),
        'exercise_weight': $("#exercise_weight").val(),
        'exercise_weightunit': $("#exercise_weightunit").val(),
        'api_exercise_equipment': $("#api_exercise_equipment").val() 
    }
        // console.log(formInputs);
    $.post("/add_exercise", formInputs, (res) => {
      // console.log(formInputs);
      addItemToTable(res.api_exercise_selection, 
                    res.exercise_sets, res.exercise_reps, 
                    res.exercise_repunit, res.exercise_info,
                    res.exercise_weight, res.exercise_weightunit, 
                    res.api_exercise_equipment);
      
    })
  });

  function changeHidden() {
    document.getElementById("hidden_exercise_form").style.visibility = "block";
    document.getElementById("hidden_workout_name").style.visibility = "none";
  }
  
  const name_wkt_button = document.querySelector('#save_workout_name');

  name_wkt_button.addEventListener('submit', () =>{
    changeHidden();
  });

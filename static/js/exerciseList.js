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
    const formInputs = {
      //'server .get requests : assign from HTML
        'exercise_selection': $("#exercise_name").val(),
        'exercise_sets': $("#exercise_sets").val(),
        'exercise_reps': $("#exercise_reps").val(),
        'exercise_repunit': $("#exercise_repunit").val(),
        'exercise_weight': $("#exercise_weight").val(),
        'exercise_weightunit': $("#exercise_weightunit").val(),
        'exercise_equipment': $("#exercise_equipment").val() 
    }

    $.post("/add_exercise", formInputs, (res) => {
      console.log(res.exercise_info);
      addItemToTable(res.exercise_selection, 
                    res.exercise_sets, res.exercise_reps, 
                    res.exercise_repunit, res.exercise_info,
                    res.exercise_weight, res.exercise_weightunit, 
                    res.exercise_equipment);
      
    })
  });



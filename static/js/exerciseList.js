"use strict";

const addItemToTable = (exercise, sets, reps) => {
    $('#user-exercise-selections').append("<tr>" +
            "<td>" + exercise + "</td>" +
            "<td>" + sets + "</td>" +
            "<td>" + reps + "</td>" +
            "</tr>");
  };

  $('#exercise-form').on('submit', (evt) => {
    evt.preventDefault();
    const formInputs = {
      //'server .get requests : assign from HTML
        'exercise_selection': $("#exercise-name").val(),
        'exercise_sets': $("#exercise_sets").val(),
        'exercise_reps': $("#exercise_reps").val()
    }
    //missing something here to, can I use 
    //formValues instead?
    // feel like I need $.post("/add_exercise") somewhere
    // addItemToTable(exercise, sets, reps);
    $.post("/add_exercise", formInputs, (res) => {
      console.log(res);
      addItemToTable(formInputs);
    })
  });


  //do I  need function to reset
  //form for user to pick new exercises??
  //
  //need to figure out how to get the correct variable 
  //in add item








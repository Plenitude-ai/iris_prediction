// // Define url to the docker service for prediction
// var url1 = 'http:{{ prediction_service_name }}/pred_args?'+"sepal_length="+{{sepal_length}}+"&sepal_width="+{{sepal_width}}"&petal_length="+{{petal_length}}+"&petal_width="+{{petal_width}};

var prediction_str =  "{{prediction}}";
document.getElementById("prediction").innerHTML = prediction_str;
// console.log({{prediction}});

// console.log('{{ oui }}')
// if("{{ oui }}" == "oui") {
//     $.ajax({
//       type: 'GET',
//       url: url1,
//       dataType: "json",
//       // headers: {
//       //   Authorization: 'Basic ' + btoa(sandboxToken)
//       // },
//       success: push_prediction_to_template,
//       error: function(xhr, textStatus, errorThrown) {
//         alert('Error when trying to process isochron: "' + textStatus + '", "' + errorThrown + '"');
//       }
//     });
// } else {
// document.getElementById("prediction").innerHTML = "No prediction"
// }
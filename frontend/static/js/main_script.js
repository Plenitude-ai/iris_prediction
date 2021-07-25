// // Define url to the docker service for prediction
// var url1 = 'http:{{ prediction_service_name }}/pred_args?'+"sepal_length="+{{sepal_length}}+"&sepal_width="+{{sepal_width}}"&petal_length="+{{petal_length}}+"&petal_width="+{{petal_width}};

var sepal_length_str =  "{{sepal_length}}";
var sepal_width_str =  "{{sepal_width}}";
var petal_length_str =  "{{petal_length}}";
var petal_width_str =  "{{petal_width}}";
document.getElementById("features").innerHTML = "For the features : sepal_length : "+sepal_length_str+" (cm), sepal_width : "+sepal_width_str+" (cm), petal_length : "+petal_length_str+" (cm), petal_width : "+petal_width_str+" (cm)"; 

var prediction_str =  "{{prediction}}";
document.getElementById("prediction").innerHTML = "The prediction is : " + prediction_str;

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
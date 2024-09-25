


/**
 * 
 */
// checkoptionselected() {
//     let d1 = document.getElementById("sa");
//     let d2 = document.getElementById("a");
//     let d3 = document.getElementById("n");
//     let d4 = document.getElementById("d");
//     let d5 = document.getElementById("da");

//     if(d1 == null && d2 == null && d3 == null && d4 == null && d5 == null){
//         document.createElement("#provideerror");
//         document.getElementById('#provideerror');
//     }
// }


document.querySelector(".options").addEventListener("hover" ,function(){
    console.log("hover");
    // document.querySelector(".options").style.cursor = pointer;
})

let question = 1;
document.querySelectorAll(".options .option").forEach(function(label) {
    label.addEventListener("click", function() {
        // Reset all label colors to black
        document.querySelectorAll(".options .option").forEach(function(l) {
            l.style.color = "black";
        });
        // Set the clicked label's color to blue
        this.querySelector("input").checked = true;
        this.style.color = "blue";
        if(question < 9){
            document.getElementById("next").click();
            question++;
        }

    });
});


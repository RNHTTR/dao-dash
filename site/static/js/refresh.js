const refresh = async () => {
    const response = await fetch('http://127.0.0.1:5000/refresh', {
        method: 'POST',
        body: "",
        // headers: {
        //     'Content-Type': 'application/json'
        // }
    })
    if (response.ok) {
      const data = await response.json();
      console.log(data);
        toastr.success("Data refreshed.", "Success", {
            timeOut:4000,
            newestOnTop:!0,
            progressBar:!0,
            preventDuplicates:false
        });
    } else {
        toastr.error("Something went wrong.", "Oops!", {
            timeOut:4000,
            newestOnTop:!0,
            progressBar:!0,
            preventDuplicates:false
        });
        console.log(response);
        document.getElementById("tokenPrice").innerHTML = "LFG"; 
        document.getElementById("tokenHolders").innerHTML = "LFG!!!";
    }
  }
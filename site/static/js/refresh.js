const refresh = async (charts) => {
    let chartMessage = ""
    switch (charts) {
      case "all":
        chartMessage += "all data";
        break
      case "chart1":
        chartMessage += "Chart 1";
        break
      case "chart2":
        chartMessage += "Chart 2";
        break
      case "chart3":
        chartMessage += "Chart 3";
        break
      case "chart4":
        chartMessage += "Chart 4";
        break
    }
    M.toast({html: `Attempting to refresh ${chartMessage}...`})

    const response = await fetch('http://127.0.0.1:5000/refresh', {
      method: 'POST',
      body: JSON.stringify({"charts": charts}),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    if (response.ok) {
      const data = await response.json();
      console.log(data);
      M.toast({html: 'Data refreshed!'})
    } else {
      M.toast({html: 'Oops!'});
      console.log(response);
    }
  }
window.onload = function() {
    refresh(cache=true);
    console.log("refreshing...")
  };

const refresh = async (cache) => {
    if (cache) {
        console.log("refreshing!")
        let tokenPrice = sessionStorage.getItem("tokenPrice");
        let tokenHolders = sessionStorage.getItem("tokenHolders");
        console.log(tokenPrice)
        if ( tokenPrice && tokenHolders ) {
            document.getElementById("tokenPrice").innerHTML = sessionStorage.getItem("tokenPrice");
            document.getElementById("tokenHolders").innerHTML = sessionStorage.getItem("tokenHolders");
            return
        }
    }
    refreshTokenPrice()
    refreshTokenHolders()
}

const refreshTokenPrice = async () => {
    document.getElementById("tokenPrice").innerHTML = '<i class="fa fa-spinner fa-pulse fa-3x fa-fw"></i>'
    const response = await fetch('http://192.168.2.9:5000/refresh/token_price', {
        method: 'POST',
        body: "",
    })
    if (response.ok) {
        const data = await response.json();
        console.log(data);
        document.getElementById("tokenPrice").innerHTML = data["token_price"];
        sessionStorage.setItem("tokenPrice", data["token_price"]);
    } else {
        document.getElementById("tokenPrice").innerHTML = "Error querying API. Try again with Dashboard -> Refresh"
        console.log(response);
    }
}

const refreshTokenHolders = async () => {
    document.getElementById("tokenHolders").innerHTML = '<i class="fa fa-spinner fa-pulse fa-3x fa-fw"></i>'
    const response = await fetch('http://192.168.2.9:5000/refresh/token_holders', {
        method: 'POST',
        body: "",
    })
    if (response.ok) {
        const data = await response.json();
        console.log(data);
        document.getElementById("tokenHolders").innerHTML = data["token_holders"];
        sessionStorage.setItem("tokenHolders", data["token_holders"]);
    } else {
        document.getElementById("tokenHolders").innerHTML = "Error querying API. Try again with Dashboard -> Refresh"
        console.log(response);
    }
}
// #    DAO Dash is a template that DAOs can use to easily create dashboards.
// #    Copyright (C) 2021 rnhttr and TylerC10
// #
// #    This program is free software: you can redistribute it and/or modify
// #    it under the terms of the GNU General Public License as published by
// #    the Free Software Foundation, either version 3 of the License, or
// #    (at your option) any later version.
// #
// #    This program is distributed in the hope that it will be useful,
// #    but WITHOUT ANY WARRANTY; without even the implied warranty of
// #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// #    GNU General Public License for more details.
// #
// #    If you don't have a copy of the GNU General Public License,
// #    see https://www.gnu.org/licenses/.

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
    const response = await fetch('http://34.73.228.17:5000/refresh/token_price', {
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
    const response = await fetch('http://34.73.228.17:5000/refresh/token_holders', {
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
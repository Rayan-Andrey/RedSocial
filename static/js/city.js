document.addEventListener("DOMContentLoaded",()=>{

    document.getElementById("btn-save").addEventListener("click",saveCity);
    function saveCity(){
        const name= document.getElementById("name").value.trim();

        if(!name){
            alert("Debe ingresar el nombre de la ciudad");
            return;
        }
        
        fetch("/cities",{
            method: "POST",
            headers:{"Content-Type" : "application/json"
            },body: JSON.stringify({
                name: name
            })
        })
        .then(response => {
            if(response.ok){
                return response.json()
            }else{
                return Promise.reject();
            }

        })
        .then(result =>{
            if(result.success){
                alert("El registro se guardo correctamente")
            }else{
                print("No se puedo guardar. Intente mas tarde")
            }
        })
    }

})
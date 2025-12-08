document.addEventListener("DOMContentLoaded", () => {

    document.getElementById("btn-save").addEventListener("click", saveUser);

    function saveUser() {
        

        const nombre = document.getElementById("nombre").value.trim();
        const correo = document.getElementById("correo").value.trim();
        const edad = document.getElementById("edad").value.trim();
        const foto = document.getElementById("foto_perfil").value.trim();

        if (!nombre) {
            alert("Debe ingresar el nombre");
            return;
        }
        if (!correo) {
            alert("Debe ingresar el correo");
            return;
        }

        fetch("/users", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                nombre: nombre,
                correo: correo,
                edad: edad || null,
                foto_perfil: foto || undefined
            })
        })
        .then(response => response.json())
        .then(result => {
            if (result.success) {
                alert("El usuario fue registrado correctamente");
                location.reload(); //DELETE SOON      
            } else {
                alert("No se pudo guardar. Intente más tarde");
            }
        })
        .catch(err => {
            console.error(err);
            alert("Error de conexión");
        });
    }

});

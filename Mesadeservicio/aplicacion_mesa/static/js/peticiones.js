// function listar_tecnicos(){
//     var url = "/listar_tecnicos/"

//     fetch (url,
//         {
//             method:"GET",
//             body:JSON.stringify(),
//             headers:{

//             }
//         }

//     )
//     .then
//     .then
// }

/* function agregar_IDcaso(id){
    // id_caso= id
    document.getElementById()
} */

function mostrarImagen(evento) {
    const archivos = evento.target.files
    const archivo = archivos[0]
    const url = URL.createObjectURL(archivo)
    const imagen = document.getElementById('imagen_mostrar')
    imagen.setAttribute('src', url)
}
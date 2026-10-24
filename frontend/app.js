const lista = document.querySelector('#ordenes');
const estado = document.querySelector('#estado');
const formulario = document.querySelector('#formulario');

async function consultarOrdenes() {
  estado.textContent = 'Consultando...';
  try {
    const respuesta = await fetch('/api/ordenes');
    if (!respuesta.ok) throw new Error(`HTTP ${respuesta.status}`);
    const resultado = await respuesta.json();
    lista.replaceChildren();
    for (const orden of resultado.data) {
      const item = document.createElement('li');
      item.textContent = `${orden.id} - ${orden.equipo}: ${orden.descripcion} [${orden.estado}]`;
      lista.append(item);
    }
    estado.textContent = `${resultado.data.length} orden(es) consultada(s)`;
  } catch (error) {
    estado.textContent = `No fue posible consultar: ${error.message}`;
  }
}

formulario.addEventListener('submit', async (evento) => {
  evento.preventDefault();
  const datos = {
    equipo: document.querySelector('#equipo').value,
    descripcion: document.querySelector('#descripcion').value
  };
  try {
    const respuesta = await fetch('/api/ordenes', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(datos)
    });
    const resultado = await respuesta.json();
    if (!respuesta.ok) throw new Error(resultado.error || `HTTP ${respuesta.status}`);
    formulario.reset();
    await consultarOrdenes();
  } catch (error) {
    estado.textContent = `No fue posible registrar: ${error.message}`;
  }
});

document.querySelector('#recargar').addEventListener('click', consultarOrdenes);
consultarOrdenes();

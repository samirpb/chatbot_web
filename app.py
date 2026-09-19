from flask import Flask, request, render_template_string

app = Flask(__name__)

def obtener_respuesta(mensaje):
    mensaje = mensaje.lower()

    if "precio" in mensaje or "750" in mensaje or "costo" in mensaje or "cuanto vale" in mensaje:
        return "Bot: El precio es $750.000"
    elif "medio de pago" in mensaje or "medios de pago" in mensaje or "pago" in mensaje or "pagos" in mensaje:
                return "Bot: aceptamos nequi, bancolombia y efectivo."
    elif "horario" in mensaje or "hora" in mensaje or "atienden" in mensaje or "abren" in mensaje:
        return "Bot: Atendemos de Lunes a Viernes de 8am a 6pm."
    elif "agendar" in mensaje or "cita" in mensaje or "agendarme" in mensaje or "dia" in mensaje:
        return "Bot: ¿Qué día quieres agendar? Escribeme el día."
    elif "chao" in mensaje or "adios" in mensaje:
        return "Bot: ¡Chao! Que tengas buen día."
    else:
        return "Bot: Prueba con 'precio', 'agendar' o 'horario'"

# HTML bonito para celular
HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Bot - Asistente Virtual</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body { font-family: Arial; background: #f0eada; padding: 10px; }
.caja { background: white; max-width: 400px; margin: auto; padding: 15px; border-radius: 15px; }
.tu { background: #dcf8c6; text-align: right; padding: 8px; border-radius: 10px; margin: 5px; }
.bot { background: #eee; padding: 8px; border-radius: 10px; margin: 5px; }
input { width: 95%; padding: 10px; border-radius: 10px; border: 2px solid black; }
button { background: #25D366; color: white; padding: 8px 15px; border: none; border-radius: 5px; margin-top: 5px; }
</style>
</head>
<body>
<div class="caja">
<h3>🤖 Bot - Asistente Virtual</h3>
<div id="chat"></div>
<input id="msg" placeholder="Escribe precio, horario...">
<button onclick="enviar()">Enviar</button>
</div>
<input id="msg" placeholder="Escribe precio, horario...">
<button onclick="enviar()">Enviar</button>
</div>
<div style="margin-top:10px; display:flex; gap:8px; justify-content:center;">
  <button onclick="enviarRapido('precio')" style="padding:6px 12px; border-radius:15px; border:1px solid #25D366; background:white; cursor:pointer;">💰 Precio</button>
  <button onclick="enviarRapido('medio de pago')" style="padding:6px 12px; border-radius:15px; border:1px solid #25D366; background:white; cursor:pointer;">💳 Pago</button>
  <button onclick="enviarRapido('horario')" style="padding:6px 12px; border-radius:15px; border:1px solid #25D366; background:white; cursor:pointer;">⏰ Horario</button>
</div>
<script>
function enviar(){enviarRapido(texto) {
  document.getElementById('msg').value = texto;
  enviar(); // llama directo a tu función que ya tienes
  let m = document.getElementById('msg').value;
  if(!m) return;
  let chat = document.getElementById('chat');
  chat.innerHTML += `<div class='tu'>Tú: ${m}</div>`;
  fetch('/chat?mensaje='+m).then(r=>r.text()).then(res=>{
    chat.innerHTML += `<div class='bot'>${res}</div>`;
  });
  document.getElementById('msg').value='';
}
</script>
</body>
</html>
"""

@app.route('/')
def inicio():
    return render_template_string(HTML)

@app.route('/chat')
def chat():
    mensaje = request.args.get('mensaje', '')
    respuesta = obtener_respuesta(mensaje)
    
    with open("conversaciones.txt", "a", encoding="utf-8") as f:
        f.write(f"Cliente: {mensaje}\n")
        f.write(f"{respuesta}\n")
    
    return respuesta

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

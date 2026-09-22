from flask import Flask, request, render_template_string
app = Flask(__name__)

def obtener_respuesta(mensaje):
    mensaje = mensaje.lower().strip()
    if "precio" in mensaje or "costo" in mensaje or "cuanto" in mensaje:
        return "Bot: El precio es $750.000"
    
    elif "pago" in mensaje or "pagos" in mensaje or "medio de pago" in mensaje or "medios de pago" in mensaje or "como pago" in mensaje :
        return " Bot: Aceptamos Nequi, Bancolombia y efectivo. Nequi: 3204523564. Bancolombia: Ahorros 123-456-789. ¿Con cuál te queda fácil?"
    
    elif "horario" in mensaje or "hora" in mensaje:
        return "Bot: Atendemos de Lunes a Viernes de 8am a 6pm."
    
    elif "agendar" in mensaje or "cita" in mensaje:
        return "Bot: ¿Qué día quieres agendar?"
    else:
        return "Bot: Prueba con 'precio', 'horario' o 'agendar'"

HTML = """
<!DOCTYPE html><html><head><title>Bot</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{font-family:Arial;background:#f0eada;padding:20px}.caja{background:white;max-width:400px;margin:auto;padding:15px;border-radius:15px} .tu{background:#dcf8c6;text-align:right;padding:8px;border-radius:10px;margin:5px} .bot{background:#eee;padding:8px;border-radius:10px;margin:5px} input{width:70%;padding:10px;border-radius:10px;border:2px solid black} button{background:#25D366;color:white;padding:10px;border:none;border-radius:5px}</style>
</head><body>
<div class="caja"><h3>🤖 Bot - Asistente Virtual</h3><div id="chat"></div>
<input id="msg" placeholder="Escribe precio, horario..."><button onclick="enviar()">Enviar</button>
<br><br>
<button onclick="enviarTexto('precio')">💰 Precio</button>
<button onclick="enviarTexto('pago')">💳 Medios de Pago</button>
<button onclick="enviarTexto('horario')">🕒 Horario</button>
<button onclick="enviarTexto('agendar')">📅 Agendar</button>
</div>
<script>
function enviarTexto(t){document.getElementById('msg').value=t; enviar();}
function enviar(){
  let m=document.getElementById('msg').value; if(!m) return;
  let chat=document.getElementById('chat');
  chat.innerHTML+=`<div class='tu'>Tú: ${m}</div>`;
  fetch('/chat?mensaje='+encodeURIComponent(m)).then(r=>r.text()).then(res=>{
    chat.innerHTML+=`<div class='bot'>${res}</div>`;
  });
  document.getElementById('msg').value='';
}
</script></body></html>
"""
@app.route('/')
def inicio(): return render_template_string(HTML)
@app.route('/chat')
def chat():
    mensaje=request.args.get('mensaje','')
    return obtener_respuesta(mensaje)
if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)

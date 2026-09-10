---
epoch: 1789051469578
mode: agent
backendId: opencode
sessionId: "ses_f799297b9ffeg1QTmZ4K8kHyEv"
agentLabel: "Plantilla de datos para boda Stephania y Yilmar"
usage: '{"usedTokens":20174,"contextWindow":1048576,"updatedAt":1789052146966}'
tags:
  - copilot-conversation
---

**user**: Estructurame una plantilla de datos:

Nombres de los novios: Stephania Manrique Sánchez y Yilmar Esaú Chávez Guerrero, Fecha: 15 de Mayo del 2027,  4:00 pm.

Lugares: Ceremonia religiosa, Capilla nuestra señora de las nieves 4:00 pm https://maps.app.goo.gl/3zSw2B9R9Ukxkj978; Recepción; Family Selection Deck 7:00 pm https://maps.app.goo.gl/eeXPLC3fwvgJU8tf8. 
Cuenta regresiva (cuenta atrás).
Mesa de regalos / datos bancarios.

    Código de vestimenta (dress code).

    Confirmación de asistencia (RSVP) vía WhatsApp directo.
[Timestamp: 2026/09/10 08:44:29]

**ai**: 
[Timestamp: 2026/09/10 08:44:29]

**user**: Estructurame una plantilla de datos:
Nombres de los novios: Stephania Manrique Sánchez y Yilmar Esaú Chávez Guerrero, Fecha: 15 de Mayo del 2027,  4:00 pm.
Lugares: Ceremonia religiosa, Capilla nuestra señora de las nieves 4:00 pm https://maps.app.goo.gl/3zSw2B9R9Ukxkj978; Recepción; Family Selection Deck 7:00 pm https://maps.app.goo.gl/eeXPLC3fwvgJU8tf8. 
Cuenta regresiva (cuenta atrás).
Mesa de regalos Liverpool 
https://mesaderegalos.liverpool.com.mx/milistaderegalos/52012979
Código de vestimenta 
Caballero: Guayabera, traje ligero, segunda imagen.
Damas: Vestido largo colores vivos, primera imagen.
Evitar colores blancos, beige y verde.
Formulario para enviar mensaje a los novios.
[Timestamp: 2026/09/10 08:51:02]

**ai**: Aquí tienes la estructura completa de datos organizada para tu invitación / sitio web de boda, tanto en formato conceptual listo para lectura como en formato técnico (JSON / JavaScript) para integrarlo directamente en tu plantilla o proyecto web.

---

### 1. Estructura Conceptual de Datos

#### 💍 Información Principal
* **Novia:** Stephania Manrique Sánchez
* **Novio:** Yilmar Esaú Chávez Guerrero
* **Fecha:** Sábado, 15 de Mayo de 2027
* **Hora de inicio:** 4:00 PM (16:00 hrs)
* **Objetivo de Cuenta Regresiva:** `2027-05-15T16:00:00`

---

#### 📍 Itinerario y Ubicaciones
1. **Ceremonia Religiosa**
   * **Lugar:** Capilla Nuestra Señora de las Nieves
   * **Hora:** 4:00 PM
   * **Ubicación GPS:** [Ver en Google Maps](https://maps.app.goo.gl/3zSw2B9R9Ukxkj978)
2. **Recepción**
   * **Lugar:** Family Selection Deck
   * **Hora:** 7:00 PM
   * **Ubicación GPS:** [Ver en Google Maps](https://maps.app.goo.gl/eeXPLC3fwvgJU8tf8)

---

#### 👗 Código de Vestimenta (Dress Code)
* **Concepto:** Formal Tropical / Elegante Colores Vivos
* **Damas:** 
  * Vestido largo en **colores vivos** (paleta *Bright Bolds*: fucsia, bugambilia, azul cielo/eléctrico, naranja, amarillo, turquesa, lila, morado).
  * *Referencia visual:* Imagen de vestidos largos y paleta de colores vivos.
* **Caballeros:** 
  * Guayabera (manga larga o corta) o traje ligero/lino.
  * *Referencia visual:* Imagen de guayaberas y tonos frescos/neutros.
* **Restricción importante:** 🚫 **Evitar estrictamente colores blanco, beige y verde.**

---

#### 🎁 Mesa de Regalos / Datos Bancarios
* **Tienda departamental:** Liverpool
* **Número de evento:** `52012979`
* **Enlace directo:** [Mesa de Regalos Liverpool](https://mesaderegalos.liverpool.com.mx/milistaderegalos/52012979)
* **Datos bancarios / Sobre:** *(Espacio disponible para agregar CLABE / Banco / Titular si se requiere)*

---

#### 📲 Confirmación de Asistencia (RSVP)
* **Canal:** WhatsApp directo.
* **Campos clave para el mensaje:**
  * Nombre(s) del invitado / familia.
  * Número de pases confirmados / declinados.
  * Mensaje de confirmación predeterminado (*ejemplo: "¡Hola Stephania y Yilmar! Confirmo mi asistencia para su boda este 15 de Mayo de 2027..."*).

---

#### 💌 Mensaje para los Novios (Libro de firmas / Formulario)
* **Campos del formulario:**
  1. Nombre completo.
  2. Correo electrónico / Teléfono.
  3. Mensaje / Deseos y felicitaciones para Stephania y Yilmar.

---

### 2. Estructura Técnica (JSON / Objeto de Configuración)

Si necesitas volcar estos datos en tu código JavaScript o consumirlos en tu plantilla HTML:

```json
{
  "wedding": {
    "couple": {
      "bride": {
        "fullName": "Stephania Manrique Sánchez",
        "shortName": "Stephania"
      },
      "groom": {
        "fullName": "Yilmar Esaú Chávez Guerrero",
        "shortName": "Yilmar"
      }
    },
    "date": {
      "displayDate": "15 de Mayo del 2027",
      "isoDate": "2027-05-15T16:00:00",
      "day": 15,
      "month": 5,
      "year": 2027,
      "time": "4:00 PM"
    },
    "events": [
      {
        "type": "Ceremonia Religiosa",
        "name": "Capilla Nuestra Señora de las Nieves",
        "time": "4:00 PM",
        "mapUrl": "https://maps.app.goo.gl/3zSw2B9R9Ukxkj978"
      },
      {
        "type": "Recepción",
        "name": "Family Selection Deck",
        "time": "7:00 PM",
        "mapUrl": "https://maps.app.goo.gl/eeXPLC3fwvgJU8tf8"
      }
    ],
    "dressCode": {
      "title": "Código de Vestimenta",
      "ladies": {
        "description": "Vestido largo en colores vivos",
        "palette": "Bright Bolds Palette",
        "imageRef": "damas-dresscode.jpg"
      },
      "gentlemen": {
        "description": "Guayabera o traje ligero",
        "imageRef": "caballeros-dresscode.jpg"
      },
      "restrictions": "Favor de evitar colores blanco, beige y verde."
    },
    "giftRegistry": {
      "store": "Liverpool",
      "eventNumber": "52012979",
      "url": "https://mesaderegalos.liverpool.com.mx/milistaderegalos/52012979",
      "bankDetails": {
        "bank": "",
        "accountHolder": "Stephania Manrique / Yilmar Chávez",
        "clabe": ""
      }
    },
    "rsvp": {
      "method": "whatsapp",
      "phone": "",
      "defaultMessage": "¡Hola Stephania y Yilmar! Confirmo con gusto mi asistencia a su boda."
    },
    "wishesForm": {
      "action": "mail-contact.php",
      "fields": ["nombre", "email", "mensaje"]
    },
    "photos": [
      "assets/images/couples/foto-estudio-pareja-1.jpg",
      "assets/images/couples/foto-manos-anillo.jpg",
      "assets/images/couples/foto-estudio-blanco-negro-1.jpg",
      "assets/images/couples/foto-estudio-sonrisa.jpg",
      "assets/images/couples/foto-estudio-abrazo.jpg",
      "assets/images/couples/foto-estudio-baile.jpg"
    ]
  }
}
```
[Timestamp: 2026/09/10 08:51:02]

**user**: Lee las especificaciones completas en @REQ-001-Adaptacion-HTML.md y ejecuta las modificaciones sobre index.html paso a paso, creando primero el respaldo index.original.html.
[Timestamp: 2026/09/10 09:06:43]

**ai**: 
[Timestamp: 2026/09/10 09:06:43]

**user**: 1. Deja un número editable de WhatsApp (ejemplo con formato internacional 521XXXXXXXXXX) con la generación dinámica del mensaje.
2. Deja listo el enlace directo a Liverpool con el evento 52012979, añade la mención de lluvia de sobres y deja el bloque editable para Banco / CLABE / Titular.
Adelante con el plan y el respaldo index.original.html.
[Timestamp: 2026/09/10 09:23:57]

**ai**: 
[Timestamp: 2026/09/10 09:23:57]
# LLM-FAQs

- Link a la App: https://ericmartinezillamola-llm-faqs.streamlit.app/

## Introducción

Este proyecto consiste en la creación de un chat bot que sea capaz de responder a preguntas frecuentes, en este caso referentes a Tesco online (servicio de delivery de UK). El chat bot funciona en Inglés.

El principal objetivo es aprender nuevas tecnologías, practicar y consolidar los conocimientos. Se trata del primer contacto con LLM (Large Language Model), por lo que es un proyecto bastante simple.

## Problemática

En la página web de la mayoría de empresas suele existir una sección de preguntas frecuentes (FAQS / Q&A), y aunque en muchos casos es algo bastante útil, también tiene ciertas limitaciones:

- Un número excesivo de preguntas frecuentes puede provocar una perdida de tiempo para los usuarios.

- Por contrapartida, si existen demasiadas pocas, no será útil para resolver muchas de las dudas que los usuarios puedan tener.

- También existen versiones alternativas, por ejemplo, disponer de un número bastante elevado de preguntas frecuentes, pero añadiendo un buscador de preguntas. Esta última alternativa tiene el inconveniente de que hay que introducir la "palabra exacta" en el buscador, en caso contario no se obtendrá el resultado deseado.

## ¿Cómo Funciona?

Este tipo de chat bots (similares a ChatGPT) pueden ser una buena alternativa a las FAQs tradicionales. El usuario introduce su pregunta, el chat bot la interpreta (entendiendo su significado y no simplemente recordando la "palabra exacta"), busca dentro de la base de datos con las preguntas y respuestas que le hemos proporcionado para comprobar si existe alguna pregunta similar, y finalmente hace una llamada a la API de GooglePaLM (el motor que usa Bard, el ChatGPT de Google) con toda la información reunida para así poder dar una respuesta coherente al usuario. Si el dataset no contiene la pregunta (ni una similar), está programado para responder "I don't know". A veces, reformular la pregunta puede ser de utilidad.

En resumen, esta opción ofrece la posibilidad de ofrecer un elevado número de preguntas frecuentes a los usuarios, pero evitando que estos tengan que perder tiempo buscando la pregunta (ya que el chat bot lo hace por ellos).

## Tecnologías y Dataset

Principales tecnologías utilizadas: LangChain, Hugging Face Embeddings, FAISS, GooglePaLM y Streamlit.

El dataset consiste en unas 100 FAQs referentes al servicio online de Tesco, el dataset es bastante reciente (30/08/2023).

Más información sobre el dataset en: https://www.kaggle.com/datasets/josephsueke/tesco-faq

Mencionar también a CodeBasics, una plataforma de e-learning muy útil para aprender nuevas tecnologías.
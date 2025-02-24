from IPython.display import Audio, display, Javascript
from google.colab import output
from base64 import b64decode

RECORD = """
  const sleep = time => new Promise(resolve => setTimeout(resolve, time))
  const b2text = blob => new Promise(resolve => {
    const reader new FileReader()
    reader.onloaded = e => resolve(e.srcElement.result)
    reader.readAsDataURL(blob)
  })

  var record = time => new Promise(async resolve => {
    stream = await navigator.mediaDevices.getUserMedia({ audio: true })
    recorder = new MediaRecorder(stream)
    chunks = []
    recorder.ondataavailable = e => chunks.push(e.data)
    recorder.start()
    await sleep(time)
    recorder.onstop = async () => {
      blob = new Blob(chunks)
      text = await b2text(blob)
      resolve(text)
    }
    recorder.stop()
  })
"""

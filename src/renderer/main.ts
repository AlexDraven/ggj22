console.log('Hello from the renderer');

const coreCount = document.getElementById('cores');

// @ts-expect-error
coreCount?.innerText = `Core count: ${api.getThreads()}`;
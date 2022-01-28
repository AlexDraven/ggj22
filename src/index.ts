import {app, ipcMain, BrowserWindow} from 'electron';

app.on('ready', initWindows);

function initWindows(): void {
    let mainWindows = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: __dirname + '/preload.js'
        },
        show: false
    });

    mainWindows.loadURL('file://' + __dirname + '/index.html');
   // mainWindows.webContents.openDevTools();
    mainWindows.on('ready-to-show', () => {
        mainWindows.show();
    });

}
const vscode = require('vscode');

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
    let showGoodNotification = vscode.commands.registerCommand('jupyter-notifier.showGoodNotification', function (message="✅ - Test Passed 🥳") {
        vscode.window.showInformationMessage(message);
    });
    let showBadNotification = vscode.commands.registerCommand('jupyter-notifier.showBadNotification', function (message="❌ - Test Failed 😭") {
        vscode.window.showInformationMessage(message);
    });

    context.subscriptions.push(showGoodNotification);
    context.subscriptions.push(showBadNotification);
}

function deactivate() {
    vscode.commands.unregisterCommand('jupyter-notifier.showGoodNotification');
    vscode.commands.unregisterCommand('jupyter-notifier.showBadNotification');
}

module.exports = {
    activate,
    deactivate
}

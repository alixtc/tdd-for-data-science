const vscode = require("vscode");

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
  let showGoodNotification = vscode.commands.registerCommand(
    "jupyter-notifier.showGoodNotification",
    function () {
      vscode.window.showInformationMessage(
        (message = "✅ Good job!"),
        (items = { title: "✅ - Test Passed 🎉" })
      );
    }
  );
  let showBadNotification = vscode.commands.registerCommand(
    "jupyter-notifier.showBadNotification",
    function () {
      vscode.window.showWarningMessage(
        (message = "❌ Try Again!"),
        (items = { title: "❌ - Test Failed 😭" })
      );
    }
  );

  context.subscriptions.push(showGoodNotification);
  context.subscriptions.push(showBadNotification);
}

function deactivate() {
  vscode.commands.unregisterCommand("jupyter-notifier.showGoodNotification");
  vscode.commands.unregisterCommand("jupyter-notifier.showBadNotification");
}

module.exports = {
  activate,
  deactivate,
};

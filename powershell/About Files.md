__________

## Display the About files content in PowerShell


Although much of the help content in Windows PowerShell relates to commands, there are also many help files that describe PowerShell concepts. These files include information about the PowerShell scripting language, operators, and other details. This information doesn't specifically relate to a single command, but to global shell techniques and features.

You can review a complete list of these topics by running:

PowerShell

```
Get-Help about*
```

To view a specific topic, use:

PowerShell

```
Get-Help about_common_parameters
```

You can also open the help topic in a separate window or online:

PowerShell

```
Get-Help about_common_parameters -ShowWindow
Get-Help about_common_parameters -Online
```

When you use wildcard characters with the **Get-Help** command, **About** help files will appear in a list when their titles contain a match for your wildcard pattern. Typically, **About** help files will appear last, after any commands whose names also matched your wildcard pattern. You can also use the _‑Category_ parameter to specify a search for **About** files.

Note

For much of this course, you'll need to refer to **About** files for additional documentation. You must review these files frequently to discover the steps and techniques you need to complete lab exercises.

### Get-Help parameters

The **Get-Help** command accepts parameters that allow you find additional information beyond the information displayed by default. A common reason to seek additional help is to identify usage examples for a command. Windows PowerShell commands commonly include many such examples. For instance, running the command **Get-Help Stop-Process –Examples** will provide examples of using the **Stop-Process** cmdlet.

The _-Full_ parameter provides in-depth information about a cmdlet, including:

- A description of each parameter.
- Whether each parameter has a default value (although this information isn't consistently documented across all commands).
- Whether a parameter is mandatory.
- Whether a parameter can accept a value in a specific position (in which case the position number, starting from 1, is given) or whether you must enter the parameter name (in which case **named** displays).
- Whether a parameter accepts pipeline input and, if so, how.

Other **Get-Help** parameters include:

- _‑ShowWindow_. Displays the help topic in a separate window, which makes it much easier to access help while entering commands.
- _‑Online_. Displays the online version of the help topic (typically the most up-to-date information) in a browser window.
- _‑Parameter ParameterName_. Displays the description of a named parameter.
- _‑Category_. Displays help only for certain categories of commands, such as cmdlets and functions.

### Show-Command

The **Show-Command** cmdlet opens a window that displays either a list of commands or a specific command's parameters. This window is the same one that displays when you select the **Show** **Command Window** option in the ISE.

To display a specific command's parameters, provide the name of the command as the value for the _‑Name_ parameter. For example, to open the **Show** **Command Window** with the command used to retrieve an Active Directory user, enter the following command in the console, and then press the Enter key:

PowerShell

```
Show-Command –Name Get-ADUser
```

The _–Name_ parameter is positional, so the following command produces the same result:

PowerShell

```
Show-Command Get-ADUser
```

If you select the **Show** **Command Window** option in the ISE, and your cursor is within or immediately next to a command name within the console or scripting pane, the results are the same.
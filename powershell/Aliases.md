____________

## Aliases and parameters

```
Get-Alias -Name
Get-Alias -del

```

It's important to note that aliases typically don't support the parameters that the original commands use. For example, if you run the command **dir /o:d** in the console, you'll receive an error because **Get‑ChildItem** doesn't recognize the _/o:d_ parameter. Instead:

```
dir | sort LastAccessTime
```


To list the contents of the current folder sorted by last accessed date and time in the ascending order.


To find all Aliases for a command

```
Get-Alias -definition Remove-Item
```

Parameters can also have aliases. For example, the _-s_ parameter is an alias for **-Recurse** in the **Get‑ChildItem** cmdlet. In fact, for parameters, you can use partial parameter names just like aliases, if the portion of the name you do include in the command is enough to uniquely identify that parameter.
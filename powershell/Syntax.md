
## Microsoft Learning

### Cmdlet Verbs
- **Get**. Retrieves a resource, such as a file or a user.
- **Set**. Changes the data associated with a resource, such as a file or user property.
- **New**. Creates a resource, such as a file or user.
- **Add**. Adds a resource to a container of multiple resources.
- **Remove**. Deletes a resource from a container of multiple resources.

**You can run the `Get-Verb` command to have the full list of approved verbs.**


### Cmd Nouns

Nouns can also have prefixes that help the grouping of related nouns into families. For example, the Active Directory nouns start with the letters **AD** (such as **ADUser**, **ADGroup**, and **ADComputer**). Microsoft SharePoint Server cmdlets begin with the prefix **SP**, and Microsoft Azure cmdlets begin with the prefix **Az**.

### Parameters

Parameters modify the actions that a cmdlet performs. You can specify no parameters, one parameter, or many parameters for a cmdlet.

- Use dash (-)
- Optional and required

### Switches

_Switches_ are a special case. They're basically parameters that accept a Boolean value (**true** or **false**). They differ from actual Boolean parameters in that the value is only set to **true** if the switch is included when running the command. An example is the _-Recurse_ parameter or switch of the **Get-ChildItem** cmdlet. The command **Get-ChildItem c:\ -Recurse** returns not just the items in the C:\ directory, but also those in all of its subdirectories. Without the **-Recurse** switch, only the items in the C:\ directory are returned.

### Tab Completion
- Speed and Learning
- Tab completion even works with wildcards. If you know you want a cmdlet that operates on services, but aren't sure which one you want, enter the text ***-service** in the console, and then press the Tab key to review all cmdlets that contain the text **-service** in their names.
### Find cmdlets in PowerShell
- **Get-Command** accepts wildcard characters, which means that you can run the **Get-Command *event*** command and retrieve a list of commands that contain the text **event** in the name.
- **Get-Command** also has several parameters that you can use to further filter the returned results. For example, you can use the _-Noun_ and _-Verb_ parameters to filter out the noun and verb portions of the name, respectively.

Both parameters accept wildcards, though in most cases you won't need to use wildcards with verbs. You can even combine the parameters to further refine the results returned. Run the **Get-Command –Noun event*** **–Verb Get** command to get a list of commands that have nouns starting with **event** and that use the **Get** verb.

### View commands within a module

 Once you know the name of the module, use `Get-Command -Module <ModuleName>` to list all commands exported by that module.
 **Ex.**
**Get-Command -Module PowerShellGet**











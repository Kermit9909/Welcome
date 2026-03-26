_______________

# PowerShell Documentation-First Learning Framework

  

## The Loop

1. Pick one cmdlet or concept  

2. Read the docs:  

   - `Get-Help <Name> -Online`  

   - `Get-Command <Name> -Syntax`  

   - `Get-Member` on the output to explore objects  

3. Run every example, then change parameters and try to break it  

4. Capture a **3-line takeaway** + 1 **gotcha** in notes  

5. Turn it into a **mini-task** you could use in the lab  

  

---

  

## Key About_Topics to Read

- about_Pipelines  

- about_Objects  

- about_Comparison_Operators  

- about_Splatting  

- about_Scopes  

- about_Profiles  

- about_Providers  

- about_Remote  

- about_Try_Catch_Finally  

  

---

  

## Core Cmdlets to Master

- `Get-Help`  

- `Get-Command`  

- `Get-Member`  

- `Select-Object`  

- `Where-Object`  

- `Sort-Object`  

- `Measure-Object`  

- `ForEach-Object`  

- `Group-Object`  

- `Export-Csv`, `Import-Csv`  

  

---

  

## Micro-Drills (Doc-Driven)

  

### Drill 1: Pipelines

- **Docs**: about_Pipelines  

- **Task**: Build a pipeline that lists the top 10 biggest files in a folder and exports results to CSV.  

- **Hint**: `Get-ChildItem -Recurse | Sort-Object Length -Descending | Select-Object -First 10 | Export-Csv .\biggest.csv -NoType`

  

---

  

### Drill 2: Searching Logs

- **Docs**: `Select-String`  

- **Task**: Search your `C:\Logs` folder for `"ERROR|FATAL"` patterns and count occurrences per file.  

- **Hint**: `Select-String -Path C:\Logs\*.log -Pattern 'ERROR|FATAL' | Group-Object Path | Select-Object Name,Count`

  

---

  

### Drill 3: Self-Healing Services

- **Docs**: `Get-Service`, `Restart-Service`  

- **Task**: Write a two-line snippet that restarts a stuck service and logs the action.  

- **Hint**:

  ```powershell

  if ((Get-Service Spooler).Status -eq 'Stopped') { Restart-Service Spooler; 'Spooler restarted' | Out-File .\service.log -Append }

  ```

  

---

  

## Note-Taking Template

- **Cmdlet/Concept**:  

- **3-Line Takeaway**:  

- **Gotcha**:  

- **Mini-Task**:
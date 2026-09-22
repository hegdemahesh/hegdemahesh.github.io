param(
    [string]$pptxFile = "c:\Users\Mahesh\Documents\GitHub\hegdemahesh.github.io\obayashi_it_presentation\Obayashi_Senior_Manager_IT_Presentation_Maheshchandra_Hegde.pptx",
    [string]$pdfFile = "c:\Users\Mahesh\Documents\GitHub\hegdemahesh.github.io\obayashi_it_presentation\Obayashi_Senior_Manager_IT_Presentation_Maheshchandra_Hegde.pdf"
)

Write-Host "Converting PPTX to PDF via PowerPoint COM..."
Write-Host "Input: $pptxFile"
Write-Host "Output: $pdfFile"

try {
    $pptApp = New-Object -ComObject PowerPoint.Application
    # Open(FileName, ReadOnly, Untitled, WithWindow)
    $presentation = $pptApp.Presentations.Open($pptxFile, 1, 0, 0)
    # ppSaveAsPDF = 32
    $presentation.SaveAs($pdfFile, 32)
    $presentation.Close()
    $pptApp.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($presentation) | Out-Null
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($pptApp) | Out-Null
    [System.GC]::Collect()
    [System.GC]::WaitForPendingFinalizers()
    Write-Host "SUCCESS: PDF successfully created at $pdfFile"
} catch {
    Write-Error "Error converting presentation to PDF: $_"
    exit 1
}

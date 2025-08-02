on run argv
    if (count of argv) = 0 then
        display dialog "Please provide the .pages file path as an argument." buttons {"OK"} default button "OK"
        return
    end if

    set filePath to item 1 of argv

    -- Extract base name and directory
    set baseName to do shell script "basename " & quoted form of filePath & " .pages"
    set dirPath to do shell script "dirname " & quoted form of filePath
    set outputPath to dirPath & "/" & baseName & ".txt"

    set theFile to POSIX file filePath

    tell application "Pages"
        activate
        open theFile

        -- Wait until at least one document is open
        repeat until (count of documents) > 0
            delay 0.2
        end repeat

        set theDoc to front document
        set docText to body text of theDoc

        close theDoc saving no
    end tell

    -- Save text to output file
    set outputFile to POSIX file outputPath as text
    set fileRef to open for access outputFile with write permission
    set eof of fileRef to 0
    write docText to fileRef
    close access fileRef

    display notification "Text exported to: " & outputPath
end run

participant_count_text = "4"
participant_count = int(participant_count_text)

if participant_count >= 4:
    print("Readiness: complete")

print("Participant count:", participant_count)

next_checkpoint = participant_count + 1
print("Next checkpoint:", next_checkpoint)

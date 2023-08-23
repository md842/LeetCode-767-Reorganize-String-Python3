"""
Leetcode 767: Reorganize String
https://leetcode.com/problems/reorganize-string/

Given a string s, rearrange the characters of s so that any two adjacent
characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Constraints:
	1 <= s.length <= 500
	s consists of lowercase English letters.
"""

from collections import Counter


def reorganizeString(s: str) -> str:
	s_dict = {}
	for ch in s:
		if ch in s_dict:
			s_dict[ch] += 1
		else:
			s_dict[ch] = 1
	count_dict = Counter(s_dict)
	mode = count_dict.most_common(1)[0][0]
	mode_count = count_dict.most_common(1)[0][1]

	# If there are at least as many occurrences of other values in s_dict as
	# there are occurrences of the most common value minus one, then a solution
	# is possible (in the worst case, we start with the most common character and
	# alternate other values between instances of the most common character)
	if (sum(s_dict.values()) - mode_count >= mode_count - 1):
		# Start with the most common item to only deal with adjacency on one side
		out_string = mode  # Set the outString to it
		last_item = mode  # Set the last item to it
		s_dict[last_item] -= 1  # Remove one occurrence from s_dict accordingly
		if (s_dict[last_item] == 0):  # If that was the only occurrence
			del s_dict[last_item]  # Remove it from s_dict
			if (s_dict and last_item == mode):  # Deleted mode and s_dict not empty
				count_dict = Counter(s_dict)  # New counter to calculate new mode
				mode = count_dict.most_common(1)[0][0]  # Calculate new mode
		for i in range(len(s) - 1):  # Construct the rest of the solution
			inserted = False  # Track whether or not insertion method was used
			if ((mode in s_dict) and (s_dict[mode] > 0) and not(last_item == mode)):
				next_item = mode  # Give priority to most common item
			else:
				my_iter = iter(s_dict)  # Get a new iterator for s_dict
				next_item = next(my_iter)  # Try first item in s_dict as next_item
				if (next_item == last_item):  # If it matches the last_item placed
					try:
						next_item = next(my_iter)  # Move iterator to next item in s_dict
					except StopIteration:
						# Check if anywhere else this character can be inserted
						inserted = False
						# If the first character is not last_item
						if not(out_string[0] == last_item):
							out_string = next_item + out_string  # Insert at beginning
							inserted = True
						else:
							for i in range(len(out_string) - 1):
								# If no last_item at this position or next position
								if (not(out_string[i] == last_item) and
	    							not(out_string[i + 1] == last_item)):
									# Insert it in this position
									out_string = out_string[:(i + 1)] + next_item +\
															 out_string[(i + 1):]
									inserted = True  # Mark as inserted
									break  # Stop searching to avoid unnecessary work
						if not(inserted):  # There was nowhere to insert, thus no solution
							return ""
			s_dict[next_item] -= 1  # Remove one occurence from s_dict accordingly
			if (s_dict[next_item] == 0):  # All occurrences of this item were used up
				del s_dict[next_item]  # Remove it from s_dict
				if (s_dict and next_item == mode):  # Deleted mode and s_dict not empty
					count_dict = Counter(s_dict)  # New counter to calculate new mode
					mode = count_dict.most_common(1)[0][0]  # Calculate new mode
			if not(inserted):  # If we didn't use the insertion method
				out_string += next_item  # Add next_item to the out_string
				last_item = next_item  # Set last_item to the one we just placed
		return out_string  # Return constructed solution
	return "" # A solution is not possible, return an empty string

# Test cases
test_cases = ["aab", "aaab", "aaabc", "aaaabcd", "aaaabbbb", "bfrbs", "zhmyo",
	      			"cxmwmmm",
							"mjpssblxurlkotcdsvzfcpttkgoonesmzulotptbbjmmftxqkchbbbaddoyfkqw"
							"ykriartdhcsxzeopeycdwwzueabsojppyhxrznxkzppyshukvxiszmrlzdcncro"
							"waiwjehovhyictrholicfhdpsmjgmdjumhxujnaobzmfacxhpnpfvbxzhnnuzlp"
							"exfpqkcuusyeqabklkmxhpwybsmypttzcdzcmmkaoruxkqleomllnhhlgqggtoy"
							"mgntzzxaxtdefpxdhgjqybkvcqzjegrvdviagjofvnxxonaknssdwcilwjkcwlt"
							"bvgwiawvaehhhoxmmiyxntkztjbhovnpuynrkdqnjchpurwuywchjclvqqhbvvt"
							"qenyzudypfeyzwdnfozvozgzisyjqhzdbrilwyylyibfjvwfcsvfmngedhcufep"
							"rzrwvbhsezftisudgtecqszipqilqncelrmrjlwtopaweidhjuzdviehti"]
test_case_expected_strings = ["aba", "", "abaca", "abacada", "abababab",
			      									"bfbrs", "zhmyo", "mcmxmwm",
															"azamzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzjzjzjz"
															"jzjzjzjzhjhjhjhjhjhjhjhjhjhjhjhphphphphphphphph"
															"phphphphphphphcpcpcpcpcpcpcpcscscscscscscscscsc"
															"scscscscscscosososobobobobobobobobobobobobobobo"
															"bobobotbtltltltltltltltltltltltltltltltltltltlt"
															"dxdxdxdxdxdxdxdxdxdxdxdxdxdxdxdxdxdxdxdudyuyuyu"
															"yuyuyuyuyuyuyuyuyuyuyuyuyuyryryryrynrnrnrnrnrnr"
															"nrnrnrnrnrnrnknknknknknknknekekekekekekekekekek"
															"evevevevevevevevevewvwvwvwvwvwvwvwvwvwvwfwfwfwf"
															"wfwfwfwfwififififififififigigigigigigigigigiqgq"
															"gqgqgqaqaqaqaqaqaqaqaqaqaqaqa"]

print()
print("Testing Report")
print("-" * 104)
num_passed = 0
for i in range(len(test_cases)):
	output = reorganizeString(test_cases[i])

	test_case_string = test_cases[i]
	if (len(test_case_string) > 20):
		test_case_string = test_case_string[:21] + "... (" +\
											 str(len(test_case_string) - 20) +\
											 " more chars)"
	print("reorganizeString(\"" + test_case_string + "\"): ", end = "")

	if (len(output) > 20):
		print(output[:21] + "... (" + str(len(output) - 20) + " more chars)")
	else:
		print(output)

	test_case_expected_string = test_case_expected_strings[i]
	if (len(test_case_expected_string) > 20):
		test_case_expected_string = test_case_expected_string[:21] +\
																"... (" +\
																str(len(test_case_expected_string) - 20) +\
																" more chars)"
	print("\\" + "-" * (11 + len(test_case_string)) + "Expected:",
        test_case_expected_string)

	if (output == test_case_expected_strings[i]):
		print("Test case", i + 1, "passed!")
		num_passed += 1
	else:
		print("Test case", i + 1, "failed!")
	print()

print("Test cases passed:", str(num_passed / len(test_cases) * 100) + "%")
print("-" * 104)
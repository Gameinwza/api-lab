# API lab results

## Part 0
- Step 0.1, number of pizza names: 18
- Step 0.3, status code without a token: 401
- Step 0.4, pizza name: The Fluffy Napoletana
- Step 0.12, results of three no-session runs (optional): [not run]
- Step 0.16, blocks for number of excluded tools: 0, 1, 2, or 3 tools; excluding all three exposes the defect.

## Defect report
- Title: Excluding every cutting tool returns an internal server error
- Request: `POST /api/pizza` with `{"excludedTools":["Knife","Pizza cutter","Scissors"]}` and the test user's token.
- Expected result: 400 with a JSON error explaining that no pizza can satisfy the request.
- Actual result: 500 with an empty body.
- Severity: Medium; a valid client input can trigger an unhandled server error, although it does not affect other users' data.

## Part A
- Step A4, status codes when the other user reads, changes, and deletes: read: 404; change: 400; delete: 400 (the owner still read 3 stars afterward).

## Part B
1. API tests can find integration failures such as incorrect routing/status codes and mismatches between HTTP responses and stored data, which stubbed unit tests cannot reveal. Unit tests still isolate logic and run quickly, making failures easier to diagnose.
2. Each test uses a new account so it owns the ratings it creates and cannot change another student's data. For a shared shop or hotel, create unique test records and only modify or delete records created by that test.
3. A session keeps the load-balancer cookie, so related requests reach the same server and can find the user created earlier. The three optional runs were not performed.
4. The all-tools-excluded block reveals the defect. A 500 signals a server failure and gives the client no useful explanation; a 400 communicates that the request cannot be satisfied. The xfail keeps the known defect visible and will alert us if the service fixes it unexpectedly.
5. Base choice needs 1 + (3−1) + (4−1) + (2−1) + (3−1) = 9 tests. All combinations need 3 × 4 × 2 × 3 = 72.
6. The other user received 404 when reading, 400 when changing, and 400 when deleting. I expected 4xx responses for all three. The API uses different 4xx codes to refuse access and confirms the rating remains unchanged for its owner.
7. The GET returned 200 and a list of ratings. This confirmed the demo accepts the made-up token for reads. If a real system accepted predictable or forged tokens, a stranger could read data accessible to the token's account. Do not use this token to create or change anything.
8. API tests check response data and status codes directly and efficiently. Only browser tests can verify what the user sees and does in the rendered interface.

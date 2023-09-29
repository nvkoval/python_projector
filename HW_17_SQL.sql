SELECT * 
FROM user_one;

SELECT *
from subscription;

INSERT INTO user_one
VALUES ('bfr548789', '2020-10-15 20:05:42', 'ger@co.com'), 
	   ('nil874596', '2020-08-09 05:19:21', 'ertn@ldo.com');

UPDATE user_one
SET email = 'red@test.com'
WHERE id = 'atb325523';

UPDATE user_one
SET create_at = '2020-01-01 11:11:12'
WHERE id = 'bnk123123';

INSERT INTO subscription
VALUES ('aas123asd', 'bnk123123', '2020-01-07 12:12:12', '2020-01-23 09:01:01', '2020-01-23 09:01:01', '2020_test', 0), 
	   ('dfg458trg', 'abj123456', '2021-02-12 12:15:15', '2021-03-10 15:08:19', '2021-03-10 15:08:19', '2021_abj', 0),
	   ('gjh875ytr', 'nil874596', '2020-09-09 07:08:08', '2020-09-15 08:18:21', '2020-09-15 08:18:21', '2020_ertn', 1),
	   ('fgh854try', 'bfr548789', '2021-01-12 21:50:12', '2021-02-04 21:08:47', '2021-02-04 21:08:47', '2021_ger', 1);
	   
SELECT user_id, email, original_purchase_date, subscription_name
FROM subscription
LEFT JOIN user_one ON (user_one.id = subscription.user_id)
WHERE is_trial = 0 
	AND DATE_PART('year', original_purchase_date) = 2020;
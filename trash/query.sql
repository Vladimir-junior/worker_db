SELECT
    `users_position`.`id`,
    `users_position`.`name`,
    COUNT(`users_user`.`id`) AS `num_users`
FROM `users_position`
LEFT OUTER JOIN `users_user` ON (`users_position`.`id` = `users_user`.`position_id`)
GROUP BY `users_position`.`id` ORDER BY NULL;


SELECT
    `users_payouts`.`id`,
    `users_payouts`.`user_id`,
    `users_payouts`.`begin_date_interval`,
    `users_payouts`.`end_date_interval`,
    `users_payouts`.`amount`,
    `users_payouts`.`status`,
    SUM(`users_bonus`.`amount`) AS `bonuses_amount`
FROM `users_payouts`
LEFT OUTER JOIN `users_bonus` ON (`users_payouts`.`id` = `users_bonus`.`payout_id`)
GROUP BY `users_payouts`.`id` ORDER BY NULL
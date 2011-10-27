select 
replace
(
	replace
	(
		replace
		(
			replace
			(
				replace
				(
					replace
					(
						replace
						(
							replace
							(
								replace
								(
									replace
									(
										replace(company_app_id::text,'217'::text,'DV verfication tag'::text),'507'::text,'TrustE notice'::text	
									),'513'::text,'DV notice'::text
								),'567'::text,'AdKeeper'::text
							),'496'::text,'AdXPose'::text
						),'586'::text,'Adometry'::text
					),'575'::text, 'Specific notice'::text
				),'568'::text, 'Evidon notice'::text
			),'599'::text, 'AdSafe pixel'::text
		),'120'::text, 'Dotomi'::text
	),'64'::text, 'Criteo'::text
),
sum(panel_daily_count)
from panel_daily
where date>='%DATE%' and 
company_app_id in(217,513,496,567,568,507,586,575,599,120,64)
group by company_app_id
order by sum(panel_daily_count) desc;
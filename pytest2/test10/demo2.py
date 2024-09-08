tuition_per_credit = float(input('请输入每学分学费金额：'))
living_expenses = float(input('请输入你每个月生活费：'))
total_credits = 17
total_tuition = total_credits * tuition_per_credit
total_cost = living_expenses * 5 + total_tuition
student_loan = total_cost * 0.6
print(f'本学期你能够贷款{student_loan:.2f}元')
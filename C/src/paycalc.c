// Pay Calculator by Aaron Gallaway (c)2022
#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>

int frequency;
float pay;
void menu1();
void menu2();
void hourly();
void weekly();
void biweekly();
void monthly();
void annually();



void main()
{
	start: ;
    int y_n = 0;
	system("cls");
	printf("Enter the pay amount: ");
	scanf("%f", &pay);
	menu1();
	printf("\n");
	printf("\nPress [1] to run again");
	printf("\nPress [2] to quit");
	printf("\n:");
	scanf("%d", &y_n);
	if (y_n == 1) {goto start;}
	else { exit(0);}
	getch();
}

void menu1() //Enter the amount of expected pay & frequency of pay
{
	printf("\n \n");
	printf("Select the frequency of pay ($%.2f):", pay);
	printf("\n [1] Hourly");
	printf("\n [2] Weekly");
	printf("\n [3] Bi-weekly");
	printf("\n [4] Monthly");
	printf("\n [5] Annually");
	printf("\n [6] Exit");
	printf("\n:");
	scanf("%d", &frequency);
	if (frequency == 6) { exit(0); }
	menu2();
}

void menu2() //Select how to calculate expected pay
{
    system("cls");
	menu: ;
	int selection;
	if ((frequency >= 1) && (frequency <= 5))
	{
		printf("Select how to calculate the pay of $%.2f: ", pay);
		if (frequency != 1) { printf("\n [1] Hourly"); }
		if (frequency != 2) { printf("\n [2] Weekly"); }
		if (frequency != 3) { printf("\n [3] Bi-weekly"); }
		if (frequency != 4) { printf("\n [4] Monthly"); }
		if (frequency != 5) { printf("\n [5] Annually"); }
		printf("\n [6] Exit");
		printf("\n:");
		scanf("%d", &selection);
	}
	else
	{
		system("cls");
		printf("\nINVALID ENTRY!");
		menu1();
	}

	switch (selection)
	{
	case 0:  //calculate all
		if (frequency != 1) { hourly(); }
		if (frequency != 2) { weekly(); }
		if (frequency != 3) { biweekly(); }
		if (frequency != 4) { monthly(); }
		if (frequency != 5) { annually(); }
		break;

	case 1:	//calculate hourly pay
		hourly();
		break;

	case 2:	//calculate weekly pay
		weekly();
		break;

	case 3:	//calculate bi-weekly pay
		biweekly();
		break;

	case 4:	//calculate monthly pay
		monthly();
		break;

	case 5:	//calculate annual pay
		annually();
		break;

	case 6:	//exit program
		exit(0);
		break;

	default:
	    system("cls");
		printf("\nINVALID ENTRY!! Please try again.");
		printf("\n");
		goto menu;
		break;
	}

}

void hourly()	//calculate hourly pay
{
	float hourlyPay;
	switch (frequency)
	{
	case 1:		//calculate hourly pay if pay rate is hourly
		hourlyPay = pay;
		break;
	case 2:		//calculate hourly pay if pay rate is weekly
		hourlyPay = pay / 40;
		break;
	case 3:		//calculate hourly pay if pay rate is bi-weekly
		hourlyPay = pay / 80;
		break;
	case 4:		//calculate hourly pay if pay rate is monthly
		hourlyPay = ((pay * 12) / 52) / 40;
		break;
	case 5:		//calculate hourly pay if pay rate is annually
		hourlyPay = (pay / 52) / 40;
		break;
	}

	printf("\nEstimated Hourly Pay:\t\t$%.2f", hourlyPay);

}

void weekly()	//calculate weekly pay
{
	float weeklyPay;
	switch (frequency)
	{
	case 1:		//calculate weekly pay if pay rate is hourly
		weeklyPay = pay * 40;
		break;
	case 2:		//calculate weekly pay if pay rate is weekly
		weeklyPay = pay;
		break;
	case 3:		//calculate weekly pay if pay rate is bi-weekly
		weeklyPay = pay / 2;
		break;
	case 4:		//calculate weekly pay if pay rate is monthly
		weeklyPay = (pay * 12) / 52;
		break;
	case 5:		//calculate weekly pay if pay rate is annually
		weeklyPay = pay / 52;
		break;
	}

	printf("\nEstimated Weekly Pay:\t\t$%.2f", weeklyPay);

}

void biweekly()	//calculate bi-weekly pay
{
	float biweeklyPay;
	switch (frequency)
	{
	case 1:		//calculate bi-weekly pay if pay rate is hourly
		biweeklyPay = pay * 80;
		break;
	case 2:		//calculate bi-weekly pay if pay rate is weekly
		biweeklyPay = pay * 2;
		break;
	case 3:		//calculate bi-weekly pay if pay rate is bi-weekly
		biweeklyPay = pay;
		break;
	case 4:		//calculate bi-weekly pay if pay rate is monthly
		biweeklyPay = ((pay * 12) / 52) * 2;
		break;
	case 5:		//calculate bi-weekly pay if pay rate is annually
		biweeklyPay = (pay / 52) * 2;
		break;
	}

	printf("\nEstimated Bi-Weekly Pay:\t$%.2f", biweeklyPay);

}

void monthly()	//calculate monthly pay
{
	float monthlyPay;
	switch (frequency)
	{
	case 1:		//calculate monthly pay if pay rate is hourly
		monthlyPay = ((pay * 40) * 52) / 12;
		break;
	case 2:		//calculate monthly pay if pay rate is weekly
		monthlyPay = (pay * 52) / 12;
		break;
	case 3:		//calculate monthly pay if pay rate is bi-weekly
		monthlyPay = (pay * 26) / 12;
		break;
	case 4:		//calculate monthly pay if pay rate is monthly
		monthlyPay = pay;
		break;
	case 5:		//calculate monthly pay if pay rate is annually
		monthlyPay = pay / 12;
		break;
	}

	printf("\nEstimated Monthly Pay:\t\t$%.2f", monthlyPay);

}

void annually()	//calculate annual pay
{
	float annualPay;
	switch (frequency)
	{
	case 1:		//calculate annual pay if pay rate is hourly
		annualPay = (pay * 40) * 52;
		break;
	case 2:		//calculate annual pay if pay rate is weekly
		annualPay = pay * 52;
		break;
	case 3:		//calculate annual pay if pay rate is bi-weekly
		annualPay = pay * 26;
		break;
	case 4:		//calculate annual pay if pay rate is monthly
		annualPay = pay * 12;
		break;
	case 5:		//calculate annual pay if pay rate is annually
		annualPay = pay;
		break;
	}

	printf("\nEstimated Annual Pay:\t\t$%.2f", annualPay);

}

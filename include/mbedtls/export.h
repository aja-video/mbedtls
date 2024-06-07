#ifndef EXPORT_H
#define EXPORT_H

#if defined(WINDOWS) && defined(BUILDING_SHARED)
	#define EXPORT __declspec(dllexport)
#else
	#define EXPORT extern
#endif

#endif
